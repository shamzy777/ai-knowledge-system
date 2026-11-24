(() => {
  const topics = Array.isArray(window.LEARNING_TOPICS) ? window.LEARNING_TOPICS : [];
  const list = document.getElementById('topic-list');

  function createMeta(label, value) {
    const group = document.createElement('div');
    const term = document.createElement('dt');
    const detail = document.createElement('dd');
    term.textContent = label;
    detail.textContent = value;
    group.append(term, detail);
    return group;
  }

  function renderTopic(topic) {
    const article = document.createElement('article');
    article.className = 'topic-card';
    article.dataset.topicId = topic.id;

    const copy = document.createElement('div');
    copy.className = 'topic-card-copy';
    const kicker = document.createElement('p');
    kicker.className = 'topic-number';
    kicker.textContent = `${topic.topicLabel}｜${topic.statusLabel}`;
    const title = document.createElement('h3');
    title.textContent = topic.title;
    const description = document.createElement('p');
    description.textContent = topic.description;
    const tags = document.createElement('ul');
    tags.className = 'topic-tags';
    tags.setAttribute('aria-label', '涵蓋概念');
    topic.conceptTags.forEach((tag) => {
      const item = document.createElement('li');
      item.textContent = tag;
      tags.append(item);
    });
    const action = document.createElement('a');
    action.className = 'hub-primary motif-button';
    action.href = topic.entryPath;
    action.textContent = '開始學習';
    copy.append(kicker, title, description, tags, action);

    const meta = document.createElement('dl');
    meta.className = 'topic-meta';
    meta.append(
      createMeta('難度', topic.difficulty),
      createMeta('時間', topic.duration),
      createMeta('形式', topic.format),
      createMeta('內容', `${topic.sections} 個學習段落`)
    );

    article.append(copy, meta);
    return article;
  }

  if (list) topics.filter((topic) => topic.status === 'available').forEach((topic) => list.append(renderTopic(topic)));

  const question = document.getElementById('hub-question');
  const mechanism = document.getElementById('hub-mechanism');
  const status = document.getElementById('hub-live-status');
  question?.addEventListener('click', () => {
    const open = mechanism?.classList.toggle('is-open') ?? false;
    question.setAttribute('aria-expanded', String(open));
    if (status) status.textContent = open
      ? '問題被拆成可以逐步觀察、操作與驗證的機制。'
      : '點一下問題，看看一個 mental model 如何展開。';
  });
})();
