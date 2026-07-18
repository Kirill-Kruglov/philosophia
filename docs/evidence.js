(() => {
  "use strict";

  const dataNode = document.getElementById("evidence-data");
  if (!dataNode) return;

  const evidence = JSON.parse(dataNode.textContent);
  const NS = "http://www.w3.org/2000/svg";

  function svgElement(name, attributes = {}, text = "") {
    const node = document.createElementNS(NS, name);
    Object.entries(attributes).forEach(([key, value]) => node.setAttribute(key, String(value)));
    if (text) node.textContent = text;
    return node;
  }

  function sourceUrl(path) {
    return "https://github.com/Kirill-Kruglov/philosophia/blob/" + evidence.sourceCommit + "/" + path;
  }

  function renderGradient() {
    const host = document.getElementById("gradient-chart");
    const width = 640;
    const height = 270;
    const left = 128;
    const right = 54;
    const top = 28;
    const plotWidth = width - left - right;
    const rowGap = 70;
    const svg = svgElement("svg", {
      viewBox: "0 0 " + width + " " + height,
      role: "img",
      "aria-label": "Horizontal bar chart. A and Opus-A share 24 wrong values of 24. A and Grok share 12 of 24. A and Gemini share 0 of 24."
    });

    [0, 6, 12, 18, 24].forEach((tick) => {
      const x = left + (tick / 24) * plotWidth;
      svg.appendChild(svgElement("line", {
        x1: x,
        y1: top,
        x2: x,
        y2: height - 38,
        class: tick === 0 ? "axis" : "gridline"
      }));
      svg.appendChild(svgElement("text", {
        x,
        y: height - 16,
        "text-anchor": "middle"
      }, String(tick)));
    });

    evidence.gradient.forEach((item, index) => {
      const y = top + 22 + index * rowGap;
      const barWidth = (item.value / item.total) * plotWidth;
      const color = index === 0 ? "#7257a5" : index === 1 ? "#b27a0d" : "#087f73";

      svg.appendChild(svgElement("text", {
        x: left - 14,
        y: y + 6,
        "text-anchor": "end",
        class: "label"
      }, item.label));

      svg.appendChild(svgElement("rect", {
        x: left,
        y: y - 12,
        width: plotWidth,
        height: 28,
        rx: 3,
        fill: "#e3e8ec"
      }));

      if (barWidth > 0) {
        svg.appendChild(svgElement("rect", {
          x: left,
          y: y - 12,
          width: barWidth,
          height: 28,
          rx: 3,
          fill: color
        }));
      } else {
        svg.appendChild(svgElement("line", {
          x1: left,
          y1: y - 12,
          x2: left,
          y2: y + 16,
          stroke: color,
          "stroke-width": 4
        }));
      }

      svg.appendChild(svgElement("text", {
        x: left + Math.max(barWidth, 8) + 10,
        y: y + 6,
        class: "value"
      }, item.value + " / " + item.total));
    });

    svg.appendChild(svgElement("text", {
      x: left + plotWidth / 2,
      y: height - 1,
      "text-anchor": "middle"
    }, "shared wrong values"));
    host.replaceChildren(svg);
  }

  function renderHoldout() {
    const body = document.getElementById("holdout-body");

    function statusCell(status) {
      const td = document.createElement("td");
      const token = document.createElement("span");
      token.className = "matrix-status " + status.toLowerCase();
      token.textContent = status;
      td.appendChild(token);
      return td;
    }

    evidence.holdout.forEach((row) => {
      const tr = document.createElement("tr");
      if (row.adverse) tr.className = "adverse";

      const arm = document.createElement("td");
      const id = document.createElement("b");
      id.textContent = row.id;
      const name = document.createElement("span");
      name.textContent = row.name;
      arm.append(id, name);

      const reading = document.createElement("td");
      reading.textContent = row.reading;

      tr.append(
        arm,
        statusCell(row.token),
        statusCell(row.journal),
        statusCell(row.combined),
        reading
      );
      body.appendChild(tr);
    });
  }

  function renderGrokking() {
    const host = document.getElementById("grokking-chart");
    const width = 900;
    const height = 400;
    const left = 88;
    const right = 70;
    const top = 38;
    const bottom = 62;
    const maxStep = 8000;
    const plotWidth = width - left - right;
    const rowGap = 54;
    const svg = svgElement("svg", {
      viewBox: "0 0 " + width + " " + height,
      role: "img",
      "aria-label": "Event map for five Arm A seeds. All fit at step 200 and generalize between steps 5200 and 7700, with delays from 5000 to 7500."
    });

    [0, 2000, 4000, 6000, 8000].forEach((tick) => {
      const x = left + (tick / maxStep) * plotWidth;
      svg.appendChild(svgElement("line", {
        x1: x,
        y1: top,
        x2: x,
        y2: height - bottom,
        class: tick === 0 ? "axis" : "gridline"
      }));
      svg.appendChild(svgElement("text", {
        x,
        y: height - 34,
        "text-anchor": "middle"
      }, tick.toLocaleString("en-US")));
    });

    evidence.level0.forEach((run, index) => {
      const y = top + 26 + index * rowGap;
      const fitX = left + (run.fit / maxStep) * plotWidth;
      const genX = left + (run.generalize / maxStep) * plotWidth;

      svg.appendChild(svgElement("text", {
        x: left - 18,
        y: y + 5,
        "text-anchor": "end",
        class: "label"
      }, run.run));

      svg.appendChild(svgElement("line", {
        x1: fitX,
        y1: y,
        x2: genX,
        y2: y,
        stroke: "#2468a2",
        "stroke-width": 6,
        "stroke-linecap": "round"
      }));

      svg.appendChild(svgElement("circle", {
        cx: fitX,
        cy: y,
        r: 8,
        fill: "#ffffff",
        stroke: "#2468a2",
        "stroke-width": 4
      }));

      svg.appendChild(svgElement("circle", {
        cx: genX,
        cy: y,
        r: 9,
        fill: "#087f73",
        stroke: "#ffffff",
        "stroke-width": 3
      }));

      svg.appendChild(svgElement("text", {
        x: genX + 14,
        y: y + 5,
        class: "value"
      }, "Δ " + run.delay.toLocaleString("en-US")));
    });

    svg.appendChild(svgElement("circle", {cx: left + 55, cy: height - 4, r: 6, fill: "#fff", stroke: "#2468a2", "stroke-width": 3}));
    svg.appendChild(svgElement("text", {x: left + 68, y: height, class: "value"}, "persistent FIT"));
    svg.appendChild(svgElement("circle", {cx: left + 205, cy: height - 4, r: 7, fill: "#087f73"}));
    svg.appendChild(svgElement("text", {x: left + 218, y: height, class: "value"}, "persistent GENERALIZE"));
    svg.appendChild(svgElement("text", {x: width - right, y: height, "text-anchor": "end"}, "training step"));

    host.replaceChildren(svg);
  }

  function renderClaims() {
    const grid = document.getElementById("claim-grid");

    evidence.claims.forEach((claim) => {
      const item = document.createElement("article");
      item.className = "claim-item";
      item.dataset.group = claim.group;

      const kicker = document.createElement("span");
      kicker.textContent = claim.kicker;
      const title = document.createElement("strong");
      title.textContent = claim.title;
      const scope = document.createElement("small");
      scope.textContent = claim.scope;

      item.append(kicker, title, scope);
      grid.appendChild(item);
    });

    document.querySelectorAll(".filter-button").forEach((button) => {
      button.addEventListener("click", () => {
        const filter = button.dataset.filter;
        document.querySelectorAll(".filter-button").forEach((candidate) => {
          const active = candidate === button;
          candidate.classList.toggle("active", active);
          candidate.setAttribute("aria-pressed", String(active));
        });
        document.querySelectorAll(".claim-item").forEach((item) => {
          item.hidden = filter !== "all" && item.dataset.group !== filter;
        });
      });
    });
  }

  function renderSources() {
    const sourceList = document.getElementById("source-list");

    Object.entries(evidence.sources).forEach(([key, source], index) => {
      document.querySelectorAll("[data-source=\"" + key + "\"]").forEach((link) => {
        link.href = sourceUrl(source.path);
      });

      const row = document.createElement("div");
      row.className = "source-entry";
      const number = document.createElement("span");
      number.textContent = String(index + 1).padStart(2, "0");
      const label = document.createElement("b");
      label.textContent = source.label;
      const link = document.createElement("a");
      link.href = sourceUrl(source.path);
      link.textContent = source.path;
      row.append(number, label, link);
      sourceList.appendChild(row);
    });
  }

  renderGradient();
  renderHoldout();
  renderGrokking();
  renderClaims();
  renderSources();
})();
