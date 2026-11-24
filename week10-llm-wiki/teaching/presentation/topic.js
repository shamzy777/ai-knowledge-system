(() => {
  const slides = Array.from(document.querySelectorAll('[data-slide]'));
  const pipelineLinks = Array.from(document.querySelectorAll('[data-pipeline-stage]'));
  const pipelineOrder = ['text', 'tokenization', 'representation', 'context', 'transformer', 'prediction', 'softmax', 'sampling', 'repeat'];
  const progress = document.getElementById('slide-progress');
  let activeIndex = 0;
  let navigationLockUntil = 0;

  function updatePipeline(slide) {
    const stage = slide?.dataset.stage || 'text';
    const stageIndex = pipelineOrder.indexOf(stage);
    let currentLink = null;
    pipelineLinks.forEach((link) => {
      const index = pipelineOrder.indexOf(link.dataset.pipelineStage);
      const isCurrent = index === stageIndex;
      link.classList.toggle('is-complete', index < stageIndex);
      if (isCurrent) {
        link.setAttribute('aria-current', 'step');
        currentLink = link;
      }
      else link.removeAttribute('aria-current');
    });
    if (currentLink && window.matchMedia('(max-width: 560px)').matches) {
      currentLink.scrollIntoView({ block: 'nearest', inline: 'center' });
    }
  }

  function updateNavigation(index) {
    activeIndex = Math.max(0, Math.min(index, slides.length - 1));
    if (progress) progress.textContent = `第 ${activeIndex + 1} / ${slides.length} 段`;
    updatePipeline(slides[activeIndex]);
  }

  function goToSlide(index) {
    const bounded = Math.max(0, Math.min(index, slides.length - 1));
    navigationLockUntil = performance.now() + 900;
    slides[bounded].scrollIntoView({ behavior: 'smooth', block: 'start' });
    updateNavigation(bounded);
    window.setTimeout(() => updateNavigation(bounded), 650);
  }

  document.addEventListener('keydown', (event) => {
    const target = event.target;
    const interactive = target instanceof HTMLElement && target.closest('input, button, summary, a, details');
    if (interactive) return;
    if (['ArrowRight', 'ArrowDown', 'PageDown'].includes(event.key)) {
      event.preventDefault();
      goToSlide(activeIndex + 1);
    }
    if (['ArrowLeft', 'ArrowUp', 'PageUp'].includes(event.key)) {
      event.preventDefault();
      goToSlide(activeIndex - 1);
    }
    if (event.key === 'Home') {
      event.preventDefault();
      goToSlide(0);
    }
    if (event.key === 'End') {
      event.preventDefault();
      goToSlide(slides.length - 1);
    }
  });

  slides.forEach((slide, index) => {
    slide.dataset.seen = index === 0 ? 'true' : 'false';
  });

  const sectionObserver = new IntersectionObserver((entries) => {
    const visible = entries
      .filter((entry) => entry.isIntersecting)
      .sort((left, right) => right.intersectionRatio - left.intersectionRatio)[0];
    entries.forEach((entry) => {
      if (entry.isIntersecting) entry.target.dataset.seen = 'true';
    });
    if (!visible) return;
    const index = slides.indexOf(visible.target);
    if (performance.now() < navigationLockUntil) return;
    if (index >= 0) updateNavigation(index);
  }, { threshold: [0.18, 0.42, 0.68], rootMargin: '-8% 0px -20% 0px' });

  slides.forEach((slide) => sectionObserver.observe(slide));
  updateNavigation(0);

  const heroButton = document.getElementById('hero-generate');
  const heroMap = document.getElementById('hero-map');
  const heroStatus = document.getElementById('hero-status');
  heroButton?.addEventListener('click', () => {
    heroMap?.classList.add('is-awake');
    if (heroStatus) heroStatus.textContent = '完整路徑已展開；接下來每一段都會說明為什麼需要下一個階段。';
    heroButton.textContent = '流程已展開';
  });

  const tokenizeButton = document.getElementById('tokenize-button');
  const tokenStream = document.getElementById('token-stream');
  tokenStream?.querySelectorAll('.token-chip').forEach((token, index) => token.style.setProperty('--i', index));
  tokenizeButton?.addEventListener('click', () => {
    tokenStream?.classList.toggle('is-tokenized');
    tokenizeButton.textContent = tokenStream?.classList.contains('is-tokenized') ? '再看一次文字轉成 tokens' : '進行 Tokenization（詞元化）';
  });

  const representationLab = document.querySelector('.representation-lab');

  function setEmbeddingStep(step) {
    if (!representationLab) return;
    representationLab.dataset.embeddingStep = String(step);
    representationLab.querySelectorAll('[data-embedding-step]').forEach((button) => {
      button.setAttribute('aria-pressed', String(Number(button.dataset.embeddingStep) === step));
    });
    representationLab.querySelectorAll('[data-embed-stage]').forEach((stage) => {
      stage.dataset.revealed = String(Number(stage.dataset.embedStage) <= step);
    });
  }

  document.querySelectorAll('[data-embedding-step]').forEach((button) => {
    button.addEventListener('click', () => setEmbeddingStep(Number(button.dataset.embeddingStep)));
  });

  document.querySelectorAll('[data-embed-token]').forEach((button) => {
    button.addEventListener('click', () => {
      document.querySelectorAll('[data-embed-token]').forEach((item) => item.setAttribute('aria-pressed', 'false'));
      button.setAttribute('aria-pressed', 'true');
      document.querySelectorAll('[data-embedding-token]').forEach((item) => {
        item.textContent = button.dataset.embedToken || '';
      });
      document.querySelectorAll('.vector-cells i').forEach((cell, index) => {
        const offset = (button.dataset.embedToken || '').length + index;
        cell.style.transform = `scaleY(${0.52 + (offset % 5) * 0.11})`;
      });
      setEmbeddingStep(1);
    });
  });
  setEmbeddingStep(1);

  const contextConnection = document.getElementById('context-connection');
  document.querySelectorAll('[data-context-choice]').forEach((button) => {
    button.addEventListener('click', () => {
      document.querySelectorAll('[data-context-choice]').forEach((item) => item.setAttribute('aria-pressed', 'false'));
      button.setAttribute('aria-pressed', 'true');
      const choice = button.dataset.contextChoice;
      if (contextConnection) contextConnection.textContent = `你把「it」與「${choice}」連起來了。模型實際計算的是可見位置之間的數值關係。`;
    });
  });

  const qkvLab = document.getElementById('qkv-demo');
  function setQkvStep(step) {
    if (!qkvLab) return;
    qkvLab.dataset.qkvStep = String(step);
    qkvLab.querySelectorAll('[data-qkv-step]').forEach((button) => {
      button.setAttribute('aria-pressed', String(Number(button.dataset.qkvStep) === step));
    });
    qkvLab.querySelectorAll('[data-qkv-panel]').forEach((panel) => {
      panel.dataset.revealed = String(Number(panel.dataset.qkvPanel) <= step);
    });
  }
  qkvLab?.querySelectorAll('[data-qkv-step]').forEach((button) => {
    button.addEventListener('click', () => setQkvStep(Number(button.dataset.qkvStep)));
  });
  setQkvStep(1);

  const attentionRow = document.getElementById('attention-token-row');
  const attentionSvg = document.getElementById('attention-lines');
  const attentionTokens = Array.from(document.querySelectorAll('[data-attention-token]'));
  const attentionLab = document.getElementById('attention-lab');

  function drawAttentionConnections() {
    if (!attentionRow || !attentionSvg) return;
    const focus = attentionTokens.find((token) => token.classList.contains('is-target')) || attentionTokens[7];
    if (!focus) return;
    const rootRect = attentionRow.getBoundingClientRect();
    const focusRect = focus.getBoundingClientRect();
    const tx = focusRect.left - rootRect.left + focusRect.width / 2;
    const ty = focusRect.bottom - rootRect.top + 14;
    attentionSvg.setAttribute('viewBox', `0 0 ${rootRect.width} ${rootRect.height}`);
    attentionSvg.replaceChildren();
    attentionTokens.forEach((token, index) => {
      if (token === focus) return;
      const rect = token.getBoundingClientRect();
      const sx = rect.left - rootRect.left + rect.width / 2;
      const sy = rect.bottom - rootRect.top + 8;
      const depth = 72 + Math.abs(sx - tx) * 0.13;
      const path = document.createElementNS('http://www.w3.org/2000/svg', 'path');
      path.setAttribute('d', `M ${sx} ${sy} C ${sx} ${sy + depth}, ${tx} ${ty + depth}, ${tx} ${ty}`);
      path.setAttribute('pathLength', '1');
      path.setAttribute('stroke-width', String(2 + (index % 3) * 1.8));
      attentionSvg.append(path);
    });
  }

  function setAttentionStep(step) {
    if (!attentionLab) return;
    attentionLab.dataset.attentionStep = String(step);
    attentionLab.querySelectorAll('[data-attention-step]').forEach((button) => {
      button.setAttribute('aria-pressed', String(Number(button.dataset.attentionStep) === step));
    });
    attentionLab.querySelectorAll('[data-attention-panel]').forEach((panel) => {
      panel.dataset.revealed = String(Number(panel.dataset.attentionPanel) <= step);
    });
    requestAnimationFrame(drawAttentionConnections);
  }
  attentionLab?.querySelectorAll('[data-attention-step]').forEach((button) => {
    button.addEventListener('click', () => setAttentionStep(Number(button.dataset.attentionStep)));
  });
  setAttentionStep(1);
  addEventListener('resize', drawAttentionConnections);
  document.fonts.ready.then(drawAttentionConnections);

  document.querySelectorAll('[data-checkpoint]').forEach((checkpoint) => {
    checkpoint.querySelectorAll('[data-checkpoint-answer]').forEach((button) => {
      button.addEventListener('click', () => {
        checkpoint.querySelectorAll('[data-checkpoint-answer]').forEach((item) => item.setAttribute('aria-pressed', 'false'));
        button.setAttribute('aria-pressed', 'true');
        const feedback = checkpoint.querySelector('.checkpoint-feedback');
        const correct = button.dataset.checkpointAnswer === 'correct';
        checkpoint.dataset.result = correct ? 'correct' : 'retry';
        if (feedback) feedback.textContent = correct
          ? '正確。你已抓到這個輸入 → 處理 → 輸出的關係。'
          : '再看一次上方的機制順序；不要只記住名詞。';
      });
    });
  });

  const zoomStage = document.querySelector('[data-zoom-stage]');
  document.querySelectorAll('[data-zoom]').forEach((button) => {
    button.addEventListener('click', () => {
      document.querySelectorAll('[data-zoom]').forEach((item) => item.setAttribute('aria-pressed', 'false'));
      button.setAttribute('aria-pressed', 'true');
      if (zoomStage) zoomStage.dataset.zoomStage = button.dataset.zoom || 'attention';
    });
  });

  const softmaxFeedback = document.getElementById('softmax-feedback');
  document.querySelectorAll('[data-softmax-prediction]').forEach((button) => {
    button.addEventListener('click', () => {
      document.querySelectorAll('[data-softmax-prediction]').forEach((item) => item.setAttribute('aria-pressed', 'false'));
      button.setAttribute('aria-pressed', 'true');
      const choice = button.dataset.softmaxPrediction;
      if (!softmaxFeedback) return;
      if (choice === 'normalize') softmaxFeedback.textContent = '正確。Softmax 把 scores 轉成非負、而且總和為一的機率。';
      if (choice === 'choose') softmaxFeedback.textContent = '選出 token 屬於下一個 Selection（選擇）階段；Softmax 停在機率分布。';
      if (choice === 'train') softmaxFeedback.textContent = '權重更新屬於 Training（訓練）；這裡呈現的是 Inference（推論）時的輸出路徑。';
    });
  });
  document.getElementById('softmax-reveal')?.addEventListener('click', () => {
    document.getElementById('softmax-lab')?.classList.toggle('is-revealed');
  });

  const decodingFeedback = document.getElementById('decoding-feedback');
  document.querySelectorAll('[data-decoding-choice]').forEach((button) => {
    button.addEventListener('click', () => {
      document.querySelectorAll('[data-decoding-choice]').forEach((item) => item.setAttribute('aria-pressed', 'false'));
      button.setAttribute('aria-pressed', 'true');
      if (!decodingFeedback) return;
      decodingFeedback.textContent = button.dataset.decodingChoice === 'sample'
        ? 'Sampling（取樣）依照分布抽取，所以低機率結果仍有可能出現。'
        : '永遠選最大值是另一種 decoding（解碼）選擇；Sampling 不保證選到最高機率 token。';
    });
  });

  const sampleResult = document.getElementById('sample-result');
  const countElements = {
    A: document.getElementById('count-a'),
    B: document.getElementById('count-b'),
    C: document.getElementById('count-c')
  };
  const counts = { A: 0, B: 0, C: 0 };
  let lastSelected = 'A';

  function drawToken() {
    const draw = Math.random();
    const token = draw < 0.70 ? 'A' : draw < 0.99 ? 'B' : 'C';
    counts[token] += 1;
    lastSelected = token;
    if (sampleResult) sampleResult.textContent = token;
    if (countElements[token]) countElements[token].textContent = String(counts[token]);
    return token;
  }

  document.getElementById('sample-again')?.addEventListener('click', drawToken);
  document.getElementById('sample-ten')?.addEventListener('click', () => {
    for (let index = 0; index < 10; index += 1) drawToken();
  });

  const loopSelected = document.getElementById('loop-selected');
  const loopHole = document.getElementById('loop-hole');
  const loopChoice = document.getElementById('loop-choice');
  const loopTransit = document.getElementById('loop-transit');
  const loopFlow = document.getElementById('loop-flow');
  const loopFeedback = document.getElementById('loop-feedback');
  const runLoopButton = document.getElementById('run-loop');
  let loopTimers = [];

  function scheduleLoopStep(callback, delay) {
    const timer = window.setTimeout(callback, delay);
    loopTimers.push(timer);
  }

  function resetLoop() {
    loopTimers.forEach((timer) => clearTimeout(timer));
    loopTimers = [];
    loopFlow?.querySelectorAll('[data-loop-stage]').forEach((stage) => {
      stage.classList.remove('is-active', 'is-complete');
    });
    if (loopChoice) loopChoice.textContent = '—';
    if (loopTransit) {
      loopTransit.textContent = '';
      loopTransit.className = 'loop-transit';
    }
    if (loopSelected) loopSelected.textContent = '';
    if (loopHole) loopHole.hidden = false;
  }

  runLoopButton?.addEventListener('click', () => {
    resetLoop();
    runLoopButton.disabled = true;
    const selected = `token ${lastSelected}`;
    const stages = Array.from(loopFlow?.querySelectorAll('[data-loop-stage]') || []);
    const reduced = matchMedia('(prefers-reduced-motion: reduce)').matches;
    const interval = reduced ? 80 : 650;
    const activate = (index, message) => {
      stages.forEach((stage, stageIndex) => {
        stage.classList.toggle('is-active', stageIndex === index);
        if (stageIndex < index) stage.classList.add('is-complete');
      });
      if (loopFeedback) loopFeedback.textContent = message;
    };

    activate(0, 'Prediction：模型先為候選 next tokens 產生 scores（分數）。');
    scheduleLoopStep(() => activate(1, 'Softmax：scores 轉成 probability distribution（機率分布），此時仍未選出 token。'), interval);
    scheduleLoopStep(() => {
      activate(2, `Selection：此時才從分布中選出 ${selected}。`);
      if (loopChoice) loopChoice.textContent = selected;
      if (loopTransit) {
        loopTransit.textContent = selected;
        loopTransit.classList.add('is-selected');
      }
    }, interval * 2);
    scheduleLoopStep(() => {
      activate(3, `Append：把 ${selected} 加入原本的 Context（上下文）。`);
      if (loopTransit) loopTransit.classList.add('is-appending');
      if (loopHole) loopHole.hidden = true;
      if (loopSelected) loopSelected.textContent = `[ ${selected} ]`;
    }, interval * 3);
    scheduleLoopStep(() => {
      activate(4, `更新完成：包含 ${selected} 的新 Context 會成為下一輪輸入。`);
      stages.forEach((stage) => stage.classList.add('is-complete'));
      if (loopTransit) loopTransit.classList.add('is-finished');
      pipelineLinks.forEach((link) => link.classList.add('is-complete'));
      runLoopButton.disabled = false;
      runLoopButton.textContent = '再運行一次循環';
    }, interval * 4);
  });

  const quizData = [
    {
      area: '完整流程', review: '#s1',
      question: '哪一個順序最能說明文字如何變成選出的 next token？',
      options: [
        '文字 → tokens → 表示 + 位置 → Context / Transformer → scores → Softmax → Sampling → 加入句子',
        '文字 → Softmax → Embedding → Sampling → Attention',
        '文字 → Sampling → tokens → Training → 機率',
        '文字 → 事實驗證 → Softmax → Tokenization'
      ],
      correct: 0,
      feedback: [
        '正確。每個階段都在解決上一個階段留下的問題。',
        'Softmax 需要先有候選 scores，所以不能出現在表示與上下文處理之前。',
        'Sampling 從分布中選擇；在 tokens 與機率出現之前，還不能取樣。',
        '事實驗證是另一個評估問題，不是 next-token selection 的必要階段。'
      ]
    },
    {
      area: 'Context / Attention', review: '#s5',
      question: '哪個說法正確區分 Query、Key 與 Value 的角色？',
      options: [
        'Query 承載全部資訊；Key 與 Value 只儲存位置。',
        'Query 與 Keys 比較；得到的權重決定如何組合 Values。',
        'Keys 選出最後 token；Values 執行 Softmax。',
        'Q、K、V 是同一個向量的三個名稱。'
      ],
      correct: 1,
      feedback: [
        'Query 參與比對，但最後被組合的資訊由 Values 承載。',
        '正確。比對角色與承載資訊的角色彼此不同。',
        '最後 token 的選擇發生在輸出機率之後，不是在 Q/K/V 內部。',
        '它們是功能不同的學習所得投影，不是同一個向量的別名。'
      ]
    },
    {
      area: 'Softmax / Sampling', review: '#s9',
      question: 'Softmax 與 Sampling（取樣）最重要的差別是什麼？',
      options: [
        'Softmax 選出 token；Sampling 更新模型權重。',
        'Softmax 與 Sampling 是同一個步驟的兩個名稱。',
        'Softmax 建立機率分布；Sampling 從中選出一個 token。',
        'Sampling 產生 scores；Softmax 把結果切成 tokens。'
      ],
      correct: 2,
      feedback: [
        '權重更新屬於 Training，而且 Softmax 不負責最後選擇。',
        '它們是輸出不同、功能不同的兩個階段。',
        '正確。先得到分布，再進行選擇。',
        'scores 來自 Language Model 的輸出路徑；Tokenization 發生在輸入端。'
      ]
    },
    {
      area: '機率推理', review: '#s10',
      question: '在 `[0.70, 0.29, 0.01]` 中，候選 C 仍可能被 Sampling 選到嗎？',
      options: ['不可能，因為它不是最大值。', '可能，因為它的機率很低但不是零。', '只有 Training 時可以。', '只有跳過 Softmax 才可以。'],
      correct: 1,
      feedback: [
        '這描述的是永遠取最大值，不是依分布進行 Sampling。',
        '正確。低機率不等於零機率。',
        '這個例子討論的是 Inference（推論）時的 token selection。',
        'Sampling 需要一個分布；跳過 Softmax 反而會失去這裡顯示的分布。'
      ]
    },
    {
      area: 'Context 轉移', review: '#s4',
      question: '如果前面的 context token 改變，後面哪些部分可能跟著改變？',
      options: [
        '只改變顯示文字；模型路徑完全不變。',
        '只改變最後 token；機率永遠不變。',
        '上下文表示、候選 scores、機率與最後選出的結果都可能改變。',
        '只改變位置資訊。'
      ],
      correct: 2,
      feedback: [
        'Context 改變時，後續使用的數值表示也可能改變。',
        '選出結果來自機率，所以機率本身也可能改變。',
        '正確。改變可能沿著整條因果路徑向後傳遞。',
        '即使位置不變，token 身分與上下文關係仍可能改變。'
      ]
    },
    {
      area: '事實依據界線', review: '#s11',
      question: '為什麼流暢的 next-token generation 不保證事實正確？',
      options: [
        '因為 Sampling 一定會製造 Hallucination。',
        '因為高機率續寫仍可能沒有事實依據或不正確。',
        '因為 Softmax 會刪除所有事實資訊。',
        '因為 Tokenization 只驗證文法。'
      ],
      correct: 1,
      feedback: [
        'Sampling 控制選擇；這裡不把它教成 Hallucination（幻覺）的原因。',
        '正確。流暢度與高機率都不等於事實驗證。',
        'Softmax 正規化 scores；它不執行事實驗證，也不會刪除事實。',
        'Tokenization 定義輸入單位；它不驗證文法或事實性。'
      ]
    }
  ];

  const quizQuestion = document.getElementById('quiz-question');
  const quizOptions = document.getElementById('quiz-options');
  const quizSubmit = document.getElementById('quiz-submit');
  const quizNext = document.getElementById('quiz-next');
  const quizFeedback = document.getElementById('quiz-feedback');
  const quizCount = document.getElementById('quiz-count');
  const quizProgressBar = document.getElementById('quiz-progress-bar');
  let quizIndex = 0;
  const quizResults = Array(quizData.length).fill(false);

  function renderQuestion() {
    const item = quizData[quizIndex];
    if (!item || !quizQuestion || !quizOptions || !quizSubmit || !quizNext || !quizFeedback) return;
    quizQuestion.textContent = item.question;
    quizOptions.replaceChildren();
    item.options.forEach((option, index) => {
      const label = document.createElement('label');
      label.className = 'quiz-option';
      const input = document.createElement('input');
      input.type = 'radio';
      input.name = 'quiz-answer';
      input.value = String(index);
      const span = document.createElement('span');
      span.textContent = option;
      label.append(input, span);
      quizOptions.append(label);
    });
    quizSubmit.disabled = true;
    quizSubmit.hidden = false;
    quizNext.hidden = true;
    quizFeedback.textContent = '請先選一個答案，再提交。';
    quizFeedback.className = 'quiz-feedback';
    if (quizCount) quizCount.textContent = `第 ${quizIndex + 1} / ${quizData.length} 題`;
    if (quizProgressBar) quizProgressBar.style.width = `${((quizIndex + 1) / quizData.length) * 100}%`;
  }

  quizOptions?.addEventListener('change', () => {
    if (quizSubmit) quizSubmit.disabled = false;
  });

  quizSubmit?.addEventListener('click', () => {
    const selected = quizOptions?.querySelector('input:checked');
    if (!(selected instanceof HTMLInputElement) || !quizFeedback || !quizNext) return;
    const selectedIndex = Number(selected.value);
    const item = quizData[quizIndex];
    const correct = selectedIndex === item.correct;
    quizFeedback.textContent = item.feedback[selectedIndex];
    quizFeedback.className = `quiz-feedback ${correct ? 'is-correct' : 'is-incorrect'}`;
    if (correct) {
      quizResults[quizIndex] = true;
      quizNext.hidden = false;
      quizNext.textContent = quizIndex === quizData.length - 1 ? '查看 mental model 回顧' : '下一題';
      quizSubmit.hidden = true;
    } else {
      const link = document.createElement('a');
      link.href = item.review;
      link.textContent = `回到「${item.area}」複習`;
      quizFeedback.append(document.createElement('br'), link);
    }
  });

  function renderQuizSummary() {
    const app = document.getElementById('quiz-app');
    if (!app) return;
    const heading = document.createElement('h3');
    heading.textContent = 'Mental model 回顧';
    const intro = document.createElement('p');
    intro.textContent = '使用複習連結回到需要再看的機制。這只是形成性回饋，不會指派或改變 mastery。';
    const summary = document.createElement('div');
    summary.className = 'quiz-summary';
    quizData.forEach((item, index) => {
      const row = document.createElement('div');
      row.className = 'quiz-summary-row';
      const label = document.createElement('span');
      label.textContent = `${item.area}｜${quizResults[index] ? '完成' : '需要複習'}`;
      const link = document.createElement('a');
      link.href = item.review;
      link.textContent = '回到對應段落';
      row.append(label, link);
      summary.append(row);
    });
    app.replaceChildren(heading, intro, summary);
  }

  quizNext?.addEventListener('click', () => {
    if (quizIndex < quizData.length - 1) {
      quizIndex += 1;
      renderQuestion();
    } else {
      renderQuizSummary();
    }
  });

  renderQuestion();
})();
