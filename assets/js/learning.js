document.documentElement.classList.add("js");

document.addEventListener("DOMContentLoaded", () => {
  const switchers = Array.from(document.querySelectorAll("[data-learning-switcher]"));

  switchers.forEach((switcher, switcherIndex) => {
    const buttons = Array.from(switcher.querySelectorAll("[data-switch-target]"));
    const scope = switcher.closest("[data-learning-scope]") || switcher.parentElement;
    const panels = Array.from(scope.querySelectorAll("[data-switch-panel]")).filter(
      (panel) => panel.closest("[data-learning-scope]") === scope,
    );
    const supplemental = Array.from(scope.querySelectorAll("[data-switch-visible]")).filter(
      (panel) => panel.closest("[data-learning-scope]") === scope,
    );
    const key = switcher.dataset.urlKey;
    const defaultValue = switcher.dataset.defaultValue || buttons[0]?.dataset.switchTarget;

    if (buttons.length === 0 || panels.length === 0 || !defaultValue) {
      return;
    }

    switcher.setAttribute("role", "tablist");
    buttons.forEach((button, buttonIndex) => {
      const panel = panels.find((item) => item.dataset.switchPanel === button.dataset.switchTarget);
      const buttonId = button.id || `learning-tab-${switcherIndex}-${buttonIndex}`;
      button.id = buttonId;
      button.setAttribute("role", "tab");
      if (panel) {
        const panelId = panel.id || `learning-panel-${switcherIndex}-${buttonIndex}`;
        panel.id = panelId;
        panel.setAttribute("role", "tabpanel");
        panel.setAttribute("aria-labelledby", buttonId);
        button.setAttribute("aria-controls", panelId);
      }
    });

    const allowed = new Set(buttons.map((button) => button.dataset.switchTarget));
    const fromUrl = key ? new URL(window.location.href).searchParams.get(key) : null;
    let selected = allowed.has(fromUrl) ? fromUrl : defaultValue;

    const updateUrl = () => {
      if (!key) {
        return;
      }
      const url = new URL(window.location.href);
      selected === defaultValue ? url.searchParams.delete(key) : url.searchParams.set(key, selected);
      window.history.replaceState({}, "", url);
    };

    const render = ({ focus = false } = {}) => {
      buttons.forEach((button) => {
        const active = button.dataset.switchTarget === selected;
        button.setAttribute("aria-selected", String(active));
        button.tabIndex = active ? 0 : -1;
        button.toggleAttribute("data-active", active);
        if (active && focus) {
          button.focus();
        }
      });

      panels.forEach((panel) => {
        panel.hidden = panel.dataset.switchPanel !== selected;
      });
      supplemental.forEach((panel) => {
        panel.hidden = !panel.dataset.switchVisible.split(" ").includes(selected);
      });
      updateUrl();
    };

    buttons.forEach((button, buttonIndex) => {
      button.addEventListener("click", () => {
        selected = button.dataset.switchTarget;
        render();
      });

      button.addEventListener("keydown", (event) => {
        let nextIndex;
        if (event.key === "ArrowRight" || event.key === "ArrowDown") {
          nextIndex = (buttonIndex + 1) % buttons.length;
        } else if (event.key === "ArrowLeft" || event.key === "ArrowUp") {
          nextIndex = (buttonIndex - 1 + buttons.length) % buttons.length;
        } else if (event.key === "Home") {
          nextIndex = 0;
        } else if (event.key === "End") {
          nextIndex = buttons.length - 1;
        } else {
          return;
        }
        event.preventDefault();
        selected = buttons[nextIndex].dataset.switchTarget;
        render({ focus: true });
      });
    });

    render();
  });
});
