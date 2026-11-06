/* ============================================================
   courses_list.js  –  Dropdown category filter for static cards
   ============================================================ */

function initFilters() {
  const select = document.getElementById("category-select");
  const grid = document.getElementById("cards-grid");
  const counter = document.getElementById("stats-count");
  if (!select || !grid) return;

  const cards = Array.from(grid.querySelectorAll(".course-card"));
  const total = cards.length;

  // Hide all cards on load until a category is chosen
  cards.forEach((card) => { card.style.display = "none"; });
  if (counter) counter.textContent = "Select a category to browse courses.";

  function applyFilter(selected) {
    let shown = 0;
    cards.forEach((card) => {
      const match = card.dataset.category === selected;
      card.style.display = match ? "" : "none";
      if (match) shown++;
    });
    if (counter) {
      counter.textContent = `Showing ${shown} course${shown !== 1 ? "s" : ""} in "${selected}"`;
    }
  }

  select.addEventListener("change", () => {
    applyFilter(select.value);
  });
}

document.addEventListener("DOMContentLoaded", initFilters);
