document.documentElement.classList.add("js");

document.addEventListener("DOMContentLoaded", () => {
  const tools = document.querySelector("[data-explorer-tools]");
  const links = Array.from(document.querySelectorAll("[data-concept-link]"));
  const sheets = Array.from(document.querySelectorAll("[data-concept-sheet]"));

  if (!tools || links.length === 0 || sheets.length === 0) {
    return;
  }

  const search = tools.querySelector("[name='q']");
  const cluster = tools.querySelector("[data-filter-cluster]");
  const source = tools.querySelector("[data-filter-source]");
  const fullOnly = tools.querySelector("[data-filter-full]");
  const resultCount = document.querySelector("[data-result-count]");
  const emptyResults = document.querySelector("[data-empty-results]");
  const clearSearch = document.querySelector("[data-clear-search]");
  const clearFilters = document.querySelector("[data-clear-filters]");
  const groups = Array.from(document.querySelectorAll("[data-concept-group]"));
  const sheetByKey = new Map(sheets.map((sheet) => [sheet.dataset.conceptSheet, sheet]));
  let selectedKey = "softmax";
  let selectionInUrl = false;
  let pathFilter = "all";
  let perspective = "integrated";

  const normalize = (value) => value.toLocaleLowerCase("en").replace(/\s+/g, " ").trim();

  links.forEach((link) => {
    const sheet = sheetByKey.get(link.dataset.conceptLink);
    link.dataset.searchText = normalize(`${link.textContent} ${sheet ? sheet.textContent : ""}`);
  });

  const readUrl = () => {
    const url = new URL(window.location.href);
    const hashValue = url.hash.slice(1);
    const hashKey = hashValue.startsWith("concept-") ? hashValue.slice(8) : hashValue;

    search.value = url.searchParams.get("q") || "";
    cluster.value = url.searchParams.get("cluster") || "all";
    source.value = url.searchParams.get("source") || "all";
    fullOnly.checked = url.searchParams.get("full") === "1";
    pathFilter = ["prerequisite", "downstream"].includes(url.searchParams.get("path")) ? url.searchParams.get("path") : "all";
    perspective = ["ai-programming", "taica"].includes(url.searchParams.get("perspective")) ? url.searchParams.get("perspective") : "integrated";
    selectionInUrl = sheetByKey.has(hashKey);
    selectedKey = selectionInUrl ? hashKey : "softmax";
  };

  const writeUrl = ({ push = false } = {}) => {
    const url = new URL(window.location.href);
    const query = search.value.trim();

    query ? url.searchParams.set("q", query) : url.searchParams.delete("q");
    cluster.value !== "all" ? url.searchParams.set("cluster", cluster.value) : url.searchParams.delete("cluster");
    source.value !== "all" ? url.searchParams.set("source", source.value) : url.searchParams.delete("source");
    fullOnly.checked ? url.searchParams.set("full", "1") : url.searchParams.delete("full");
    pathFilter === "all" ? url.searchParams.delete("path") : url.searchParams.set("path", pathFilter);
    perspective === "integrated" ? url.searchParams.delete("perspective") : url.searchParams.set("perspective", perspective);
    url.hash = selectionInUrl ? `concept-${selectedKey}` : "";

    window.history[push ? "pushState" : "replaceState"]({}, "", url);
  };

  const classifyPathRows = (sheet) => {
    const title = normalize(sheet.querySelector("h2")?.textContent || "");
    return Array.from(sheet.querySelectorAll(".supported-paths li")).map((row) => {
      const items = Array.from(row.children);
      const selectedIndex = items.findIndex((item) => item.tagName === "STRONG" && normalize(item.textContent).startsWith(title));
      const relation = normalize(row.querySelector(".relationship-label")?.textContent || "");
      const kind = selectedIndex > 0 && relation === "prerequisite"
        ? "prerequisite"
        : selectedIndex === 0 && relation !== "contrast"
          ? "downstream"
          : "other";
      row.dataset.pathKind = kind;
      return row;
    });
  };

  const installPathControls = () => {
    const template = document.querySelector("#path-controls-template");
    if (!template) {
      return;
    }
    sheets.forEach((sheet) => {
      const section = sheet.querySelector(".supported-paths");
      if (!section || section.querySelector(".path-controls")) {
        return;
      }
      section.querySelector("h3")?.insertAdjacentElement("afterend", template.content.firstElementChild.cloneNode(true));
      const rows = classifyPathRows(sheet);
      section.querySelectorAll("[data-path-filter]").forEach((button) => {
        const requested = button.dataset.pathFilter;
        if (requested !== "all" && !rows.some((row) => row.dataset.pathKind === requested)) {
          button.disabled = true;
        }
      });
    });
  };

  const installPerspectiveControls = () => {
    const template = document.querySelector("#perspective-controls-template");
    if (!template) {
      return;
    }
    sheets.forEach((sheet) => {
      const section = sheet.querySelector(".cross-course-lens");
      if (!section || section.querySelector(".perspective-controls")) {
        return;
      }
      section.querySelector("h3")?.insertAdjacentElement("afterend", template.content.firstElementChild.cloneNode(true));
    });
  };

  const renderLearningControls = () => {
    const sheet = sheetByKey.get(selectedKey);
    if (!sheet) {
      return;
    }

    const pathButtons = Array.from(sheet.querySelectorAll("[data-path-filter]"));
    if (!pathButtons.some((button) => button.dataset.pathFilter === pathFilter && !button.disabled)) {
      pathFilter = "all";
    }
    pathButtons.forEach((button) => {
      const active = button.dataset.pathFilter === pathFilter;
      button.toggleAttribute("data-active", active);
      button.setAttribute("aria-pressed", String(active));
    });
    sheet.querySelectorAll("[data-path-kind]").forEach((row) => {
      row.toggleAttribute("data-path-muted", pathFilter !== "all" && row.dataset.pathKind !== pathFilter);
      row.toggleAttribute("data-path-highlighted", pathFilter !== "all" && row.dataset.pathKind === pathFilter);
    });

    const perspectiveButtons = Array.from(sheet.querySelectorAll("[data-perspective]"));
    perspectiveButtons.forEach((button) => {
      const active = button.dataset.perspective === perspective;
      button.toggleAttribute("data-active", active);
      button.setAttribute("aria-pressed", String(active));
    });
    sheet.querySelectorAll("[data-perspective-panel]").forEach((panel) => {
      const panelPerspective = panel.dataset.perspectivePanel;
      const visible = perspective === "integrated" || panelPerspective === perspective;
      panel.hidden = !visible;
    });
  };

  const showSelected = ({ focus = false, scroll = false } = {}) => {
    sheets.forEach((sheet) => {
      const isSelected = sheet.dataset.conceptSheet === selectedKey;
      sheet.hidden = !isSelected;
      sheet.toggleAttribute("data-selected", isSelected);
    });

    links.forEach((link) => {
      const isSelected = link.dataset.conceptLink === selectedKey;
      if (isSelected) {
        link.setAttribute("aria-current", "true");
      } else {
        link.removeAttribute("aria-current");
      }
    });

    const sheet = sheetByKey.get(selectedKey);
    if (!sheet) {
      return;
    }

    const heading = sheet.querySelector("h2");
    if (heading) {
      heading.tabIndex = -1;
      if (focus) {
        heading.focus({ preventScroll: true });
      }
    }

    if (scroll && window.matchMedia("(max-width: 60rem)").matches) {
      sheet.scrollIntoView({ block: "start" });
    }
    renderLearningControls();
  };

  const applyFilters = ({ updateUrl = true } = {}) => {
    const query = normalize(search.value);
    let visibleCount = 0;

    links.forEach((link) => {
      const clusterMatch = cluster.value === "all" || link.dataset.cluster.split(" ").includes(cluster.value);
      const sourceMatch = source.value === "all" || link.dataset.sources.split(" ").includes(source.value);
      const tierMatch = !fullOnly.checked || link.dataset.tier === "tier-1";
      const queryMatch = !query || link.dataset.searchText.includes(query);
      const visible = clusterMatch && sourceMatch && tierMatch && queryMatch;

      link.hidden = !visible;
      if (visible) {
        visibleCount += 1;
      }
    });

    groups.forEach((group) => {
      const hasVisibleLink = Array.from(group.querySelectorAll("[data-concept-link]")).some((link) => !link.hidden);
      group.hidden = !hasVisibleLink;
    });

    resultCount.textContent = `${visibleCount} ${visibleCount === 1 ? "concept" : "concepts"}`;
    emptyResults.hidden = visibleCount !== 0;

    if (visibleCount === 0) {
      sheets.forEach((sheet) => {
        sheet.hidden = true;
        sheet.removeAttribute("data-selected");
      });
      links.forEach((link) => link.removeAttribute("aria-current"));
      if (updateUrl) {
        writeUrl();
      }
      return;
    }

    const selectedLink = links.find((link) => link.dataset.conceptLink === selectedKey);
    if (!selectedLink || selectedLink.hidden) {
      selectedKey = links.find((link) => !link.hidden).dataset.conceptLink;
    }

    showSelected();
    if (updateUrl) {
      writeUrl();
    }
  };

  const selectConcept = (key, { push = true, focus = true, scroll = true } = {}) => {
    if (!sheetByKey.has(key)) {
      return;
    }
    selectedKey = key;
    selectionInUrl = true;
    showSelected({ focus, scroll });
    writeUrl({ push });
  };

  document.addEventListener("click", (event) => {
    const pathButton = event.target.closest("[data-path-filter]");
    if (pathButton && !pathButton.disabled) {
      pathFilter = pathButton.dataset.pathFilter;
      renderLearningControls();
      writeUrl();
      return;
    }

    const perspectiveButton = event.target.closest("[data-perspective]");
    if (perspectiveButton) {
      perspective = perspectiveButton.dataset.perspective;
      renderLearningControls();
      writeUrl();
      return;
    }

    const anchor = event.target.closest("a[href^='#concept-']");
    if (!anchor) {
      return;
    }

    const key = anchor.getAttribute("href").slice(9);
    if (!sheetByKey.has(key)) {
      return;
    }

    event.preventDefault();
    selectConcept(key);
  });

  search.addEventListener("input", () => applyFilters());
  cluster.addEventListener("change", () => applyFilters());
  source.addEventListener("change", () => applyFilters());
  fullOnly.addEventListener("change", () => applyFilters());

  clearSearch.addEventListener("click", () => {
    search.value = "";
    applyFilters();
    search.focus();
  });

  clearFilters.addEventListener("click", () => {
    search.value = "";
    cluster.value = "all";
    source.value = "all";
    fullOnly.checked = false;
    applyFilters();
    search.focus();
  });

  window.addEventListener("popstate", () => {
    readUrl();
    applyFilters({ updateUrl: false });
    showSelected();
  });

  installPathControls();
  installPerspectiveControls();
  readUrl();
  applyFilters({ updateUrl: false });
  showSelected();
  writeUrl();
});
