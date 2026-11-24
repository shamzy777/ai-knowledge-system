#!/usr/bin/env node
// Browser validation for the Week 10 Learning Hub and Topic 01.
import { mkdirSync, writeFileSync } from 'node:fs';
import { resolve, dirname } from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';
import { Browser, sleep } from '/Users/shamzylee/.codex/skills/taste-skill/scripts/lib/cdp.mjs';

const root = resolve(dirname(fileURLToPath(import.meta.url)), '../..');
const hubPath = resolve(root, 'teaching/presentation/index.html');
const topicPath = resolve(root, 'teaching/presentation/topics/next-token.html');
const outDir = resolve(root, 'teaching/presentation/validation/screenshots');
const reportPath = resolve(root, 'teaching/presentation/validation/render-report.json');
mkdirSync(outDir, { recursive: true });

const viewports = [
  { width: 375, height: 812 },
  { width: 768, height: 1024 },
  { width: 1280, height: 800 },
  { width: 1440, height: 900 },
  { width: 1920, height: 1080 },
];

const report = {
  at: new Date().toISOString(),
  urls: { hub: pathToFileURL(hubPath).href, topic: pathToFileURL(topicPath).href },
  architecture: {}, hubViewports: [], topicViewports: [], interactions: {}, noJavaScript: {}, result: 'PASS'
};
const failures = [];
const browser = await Browser.launch();

function noteFailure(message) { failures.push(message); report.result = 'FAIL'; }

async function measurePage(page, type) {
  return page.eval((pageType) => {
    const nodes = [...document.querySelectorAll('body *')].filter((node) => {
      const style = getComputedStyle(node); const rect = node.getBoundingClientRect();
      return style.display !== 'none' && style.visibility !== 'hidden' && rect.width > 0 && rect.height > 0;
    });
    const horizontalOffenders = nodes.filter((node) => {
      if (node.closest('.pipeline-nav')) return false;
      const rect = node.getBoundingClientRect();
      return rect.left < -1 || rect.right > innerWidth + 1;
    }).slice(0, 10).map((node) => ({ tag: node.tagName, className: node.className, text: (node.textContent || '').trim().slice(0, 80), rect: node.getBoundingClientRect().toJSON() }));
    return {
      pageType, innerWidth, scrollWidth: document.documentElement.scrollWidth, horizontalOffenders,
      bodyHeight: document.body.scrollHeight, h1Count: document.querySelectorAll('h1').length,
      topicCards: document.querySelectorAll('[data-topic-id]').length,
      slideCount: document.querySelectorAll('[data-slide]').length,
      evidenceCount: document.querySelectorAll('[data-slide] .evidence').length,
      documentLanguage: document.documentElement.lang
    };
  }, type);
}

async function validateResponsivePage(type, url, viewport) {
  const page = await browser.newPage({ ...viewport, mobile: viewport.width < 600, reducedMotion: true });
  await page.goto(url, { settleMs: 500 });
  await page.eval('document.fonts.ready.then(() => true)');
  const metrics = await measurePage(page, type);
  const screenshot = resolve(outDir, `${type}-${viewport.width}.png`);
  await page.screenshot({ path: screenshot, format: 'png', fullPage: true });
  const item = { ...viewport, ...metrics, consoleErrors: page.consoleErrors, screenshot };
  if (metrics.scrollWidth > metrics.innerWidth + 1 || metrics.horizontalOffenders.length) noteFailure(`${type} horizontal overflow at ${viewport.width}px`);
  if (metrics.h1Count !== 1) noteFailure(`${type} must contain exactly one h1 at ${viewport.width}px`);
  if (metrics.documentLanguage !== 'zh-Hant') noteFailure(`${type} language is not zh-Hant at ${viewport.width}px`);
  if (page.consoleErrors.length) noteFailure(`${type} console errors at ${viewport.width}px: ${page.consoleErrors.join('; ')}`);
  if (type === 'hub' && metrics.topicCards !== 1) noteFailure(`hub did not render exactly one active topic card at ${viewport.width}px`);
  if (type === 'topic' && (metrics.slideCount !== 11 || metrics.evidenceCount !== 11)) noteFailure(`topic missing slides/evidence at ${viewport.width}px`);
  await page.close();
  return item;
}

try {
  for (const viewport of viewports) {
    report.hubViewports.push(await validateResponsivePage('hub', report.urls.hub, viewport));
    report.topicViewports.push(await validateResponsivePage('topic', report.urls.topic, viewport));
  }

  const hub = await browser.newPage({ width: 1280, height: 800, reducedMotion: true });
  await hub.goto(report.urls.hub, { settleMs: 350 });
  report.architecture = await hub.eval(() => {
    const topicLink = document.querySelector('[data-topic-id="topic-01"] a[href]');
    return {
      title: document.title,
      topicCards: document.querySelectorAll('[data-topic-id]').length,
      topicHref: topicLink?.getAttribute('href') || '',
      topicResolved: topicLink?.href || '',
      futurePlaceholder: document.body.textContent.includes('更多主題持續加入中')
    };
  });
  if (report.architecture.topicHref !== 'topics/next-token.html' || !report.architecture.futurePlaceholder) noteFailure('hub architecture or Topic 01 entry is incomplete');
  report.interactions.hub = await hub.eval(() => {
    document.getElementById('hub-question').click();
    return {
      expanded: document.getElementById('hub-question').getAttribute('aria-expanded'),
      open: document.getElementById('hub-mechanism').classList.contains('is-open'),
      status: document.getElementById('hub-live-status').textContent
    };
  });
  if (report.interactions.hub.expanded !== 'true' || !report.interactions.hub.open) noteFailure('hub mental-model interaction did not open');
  await hub.close();

  const page = await browser.newPage({ width: 1280, height: 800, reducedMotion: true });
  await page.goto(report.urls.topic, { settleMs: 350 });
  report.architecture.topicReturnHome = await page.eval(() => document.querySelector('.return-home')?.getAttribute('href') || '');
  if (report.architecture.topicReturnHome !== '../index.html') noteFailure('Topic 01 return-home link is incorrect');
  await page.eval("document.getElementById('s1').scrollIntoView({block:'start'})");
  await sleep(120);
  await page.send('Input.dispatchKeyEvent', { type: 'keyDown', key: 'ArrowDown', code: 'ArrowDown' });
  await page.send('Input.dispatchKeyEvent', { type: 'keyUp', key: 'ArrowDown', code: 'ArrowDown' });
  await sleep(750);
  report.interactions.keyboardProgress = await page.eval("document.getElementById('slide-progress').textContent");
  if (report.interactions.keyboardProgress !== '第 2 / 11 段') noteFailure('ArrowDown keyboard navigation did not advance to section 2');

  report.interactions.pipeline = await page.eval(() => {
    const el = document.querySelector('[data-pipeline-stage="softmax"]'); el.click();
    return { href: el.getAttribute('href'), hash: location.hash, targetExists: Boolean(document.querySelector(el.getAttribute('href'))) };
  });
  if (report.interactions.pipeline.hash !== '#s9' || !report.interactions.pipeline.targetExists) noteFailure('pipeline navigation did not route to Softmax');

  report.interactions.embedding = await page.eval(() => {
    document.querySelector('button[data-embedding-step="4"]').click();
    document.querySelector('[data-checkpoint="embedding"] [data-checkpoint-answer="correct"]').click();
    return {
      step: document.querySelector('.representation-lab').dataset.embeddingStep,
      revealed: document.querySelectorAll('[data-embed-stage][data-revealed="true"]').length,
      positionVisible: getComputedStyle(document.querySelector('.position-combine')).display !== 'none',
      checkpoint: document.querySelector('[data-checkpoint="embedding"] .checkpoint-feedback').textContent
    };
  });
  if (report.interactions.embedding.step !== '4' || report.interactions.embedding.revealed !== 4 || !report.interactions.embedding.positionVisible || !report.interactions.embedding.checkpoint.includes('正確。')) noteFailure('Embedding progressive mechanism or checkpoint failed');

  report.interactions.qkv = await page.eval(() => {
    document.querySelector('button[data-qkv-step="5"]').click();
    document.querySelector('[data-checkpoint="qkv"] [data-checkpoint-answer="correct"]').click();
    return {
      step: document.getElementById('qkv-demo').dataset.qkvStep,
      revealed: document.querySelectorAll('[data-qkv-panel][data-revealed="true"]').length,
      distinction: document.querySelector('.qkv-distinction').textContent,
      checkpoint: document.querySelector('[data-checkpoint="qkv"] .checkpoint-feedback').textContent
    };
  });
  if (report.interactions.qkv.step !== '5' || report.interactions.qkv.revealed !== 5 || !report.interactions.qkv.distinction.includes('決定相關程度') || !report.interactions.qkv.checkpoint.includes('正確。')) noteFailure('Q/K/V progressive mechanism or checkpoint failed');

  report.interactions.attention = await page.eval(() => {
    document.querySelector('button[data-attention-step="6"]').click();
    document.querySelector('[data-checkpoint="attention"] [data-checkpoint-answer="correct"]').click();
    return {
      step: document.getElementById('attention-lab').dataset.attentionStep,
      revealed: document.querySelectorAll('[data-attention-panel][data-revealed="true"]').length,
      after: document.querySelector('[data-attention-final]').textContent,
      checkpoint: document.querySelector('[data-checkpoint="attention"] .checkpoint-feedback').textContent
    };
  });
  if (report.interactions.attention.step !== '6' || report.interactions.attention.revealed !== 6 || !report.interactions.attention.after.includes('更新後') || !report.interactions.attention.checkpoint.includes('正確。')) noteFailure('Self-Attention progressive mechanism or checkpoint failed');

  report.interactions.transformerZoom = await page.eval(() => {
    document.querySelector('button[data-zoom="model"]').click();
    const visible = [...document.querySelectorAll('[data-zoom-view]')].filter((view) => getComputedStyle(view).display !== 'none');
    return { stage: document.querySelector('[data-zoom-stage]').dataset.zoomStage, visible: visible.length, text: visible[0]?.textContent || '' };
  });
  if (report.interactions.transformerZoom.stage !== 'model' || report.interactions.transformerZoom.visible !== 1 || !report.interactions.transformerZoom.text.includes('Self-Attention 在這裡')) noteFailure('Transformer zoom hierarchy failed');

  report.interactions.sampling = await page.eval(() => {
    document.getElementById('sample-again').click();
    const result = document.getElementById('sample-result').textContent;
    const total = ['count-a', 'count-b', 'count-c'].map((id) => Number(document.getElementById(id).textContent)).reduce((a, b) => a + b, 0);
    return { result, total };
  });
  if (!['A', 'B', 'C'].includes(report.interactions.sampling.result) || report.interactions.sampling.total !== 1) noteFailure('sampling interaction did not record one draw');
  report.interactions.samplingTen = await page.eval(() => {
    document.getElementById('sample-ten').click();
    return ['count-a', 'count-b', 'count-c'].map((id) => Number(document.getElementById(id).textContent)).reduce((a, b) => a + b, 0);
  });
  if (report.interactions.samplingTen !== 11) noteFailure('10× sampling did not add ten draws');

  report.interactions.loopInitial = await page.eval(() => ({
    selected: document.getElementById('loop-selected').textContent,
    holeVisible: !document.getElementById('loop-hole').hidden,
    choice: document.getElementById('loop-choice').textContent
  }));
  if (report.interactions.loopInitial.selected.trim() || !report.interactions.loopInitial.holeVisible || report.interactions.loopInitial.choice !== '—') noteFailure('repeat loop reveals a token before Selection');
  await page.eval("document.getElementById('run-loop').click()");
  await sleep(650);
  report.interactions.loopComplete = await page.eval(() => ({
    selected: document.getElementById('loop-selected').textContent,
    holeHidden: document.getElementById('loop-hole').hidden,
    choice: document.getElementById('loop-choice').textContent,
    completedStages: document.querySelectorAll('[data-loop-stage].is-complete').length,
    button: document.getElementById('run-loop').textContent,
    feedback: document.getElementById('loop-feedback').textContent
  }));
  if (!report.interactions.loopComplete.selected.includes('token ') || !report.interactions.loopComplete.holeHidden || !report.interactions.loopComplete.choice.includes('token ') || report.interactions.loopComplete.completedStages !== 5 || report.interactions.loopComplete.button !== '再運行一次循環' || !report.interactions.loopComplete.feedback.includes('下一輪輸入')) noteFailure('repeat loop causal state machine failed');

  report.interactions.quiz = await page.eval(() => {
    const first = document.querySelector('#quiz-options input[value="0"]'); first.click(); first.dispatchEvent(new Event('change', { bubbles: true }));
    document.getElementById('quiz-submit').click();
    return { feedback: document.getElementById('quiz-feedback').textContent, nextHidden: document.getElementById('quiz-next').hidden };
  });
  if (!report.interactions.quiz.feedback.includes('正確。') || report.interactions.quiz.nextHidden) noteFailure('Traditional Chinese quiz feedback failed');
  await page.screenshot({ path: resolve(outDir, 'topic-mechanisms-expanded-1280.png'), format: 'png', fullPage: true });
  await page.close();

  const noJsHub = await browser.newPage({ width: 375, height: 812, mobile: true, reducedMotion: true });
  await noJsHub.send('Emulation.setScriptExecutionDisabled', { value: true });
  await noJsHub.goto(report.urls.hub, { settleMs: 250 });
  report.noJavaScript.hub = await noJsHub.eval(() => ({
    className: document.documentElement.className,
    topicFallback: document.body.textContent.includes('LLM 是怎麼產生下一個 token 的？'),
    textLength: document.body.innerText.trim().length,
    scrollWidth: document.documentElement.scrollWidth, innerWidth
  }));
  await noJsHub.screenshot({ path: resolve(outDir, 'hub-375-no-js.png'), format: 'png', fullPage: true });
  if (report.noJavaScript.hub.className !== 'no-js' || !report.noJavaScript.hub.topicFallback || report.noJavaScript.hub.textLength < 300 || report.noJavaScript.hub.scrollWidth > report.noJavaScript.hub.innerWidth + 1) noteFailure('hub no-JavaScript fallback is incomplete');
  await noJsHub.close();

  const noJsTopic = await browser.newPage({ width: 375, height: 812, mobile: true, reducedMotion: true });
  await noJsTopic.send('Emulation.setScriptExecutionDisabled', { value: true });
  await noJsTopic.goto(report.urls.topic, { settleMs: 250 });
  report.noJavaScript.topic = await noJsTopic.eval(() => ({
    className: document.documentElement.className,
    slides: document.querySelectorAll('[data-slide]').length,
    visibleSlides: [...document.querySelectorAll('[data-slide]')].filter((el) => getComputedStyle(el).display !== 'none').length,
    opaqueSlides: [...document.querySelectorAll('[data-slide]')].filter((el) => Number(getComputedStyle(el).opacity) > 0.99).length,
    textLength: document.body.innerText.trim().length,
    wikiLinks: document.querySelectorAll('a[href^="../../../wiki/"]').length,
    quizItems: document.querySelectorAll('.quiz-list details').length,
    fallbackText: document.body.textContent.includes('沒有 JavaScript 時'),
    scrollWidth: document.documentElement.scrollWidth, innerWidth
  }));
  await noJsTopic.screenshot({ path: resolve(outDir, 'topic-375-no-js.png'), format: 'png', fullPage: true });
  const topicFallback = report.noJavaScript.topic;
  if (topicFallback.className !== 'no-js' || topicFallback.slides !== 11 || topicFallback.visibleSlides !== 11 || topicFallback.opaqueSlides !== 11 || topicFallback.textLength < 2000 || topicFallback.wikiLinks !== 31 || topicFallback.quizItems !== 6 || !topicFallback.fallbackText || topicFallback.scrollWidth > topicFallback.innerWidth + 1) noteFailure('topic no-JavaScript fallback is incomplete');
  await noJsTopic.close();
} finally {
  await browser.close();
}

report.failures = failures;
writeFileSync(reportPath, JSON.stringify(report, null, 2) + '\n');
console.log(JSON.stringify(report, null, 2));
process.exit(failures.length ? 1 : 0);
