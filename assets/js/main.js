// Mobile nav toggle
document.addEventListener('DOMContentLoaded', function () {
  var toggle = document.querySelector('.nav-toggle');
  var links = document.querySelector('.nav-links');
  if (toggle && links) {
    toggle.addEventListener('click', function () {
      links.classList.toggle('open');
      var expanded = links.classList.contains('open');
      toggle.setAttribute('aria-expanded', expanded ? 'true' : 'false');
    });
  }

  // Accordion (homepage research areas)
  document.querySelectorAll('.accordion-header').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var item = btn.closest('.accordion-item');
      item.classList.toggle('open');
      var expanded = item.classList.contains('open');
      btn.setAttribute('aria-expanded', expanded ? 'true' : 'false');
    });
  });

  // Publications tab filter
  var tabStrip = document.querySelector('.tab-strip');
  if (tabStrip) {
    var items = Array.prototype.slice.call(document.querySelectorAll('.pub-item'));
    var countEl = document.querySelector('.result-count');

    function applyFilter(tab) {
      var visible = 0;
      items.forEach(function (item) {
        var tabs = (item.getAttribute('data-tab') || '').split(' ');
        var show = tab === 'all' || tabs.indexOf(tab) !== -1;
        item.classList.toggle('hidden', !show);
        if (show) visible++;
      });
      if (countEl) countEl.textContent = visible + ' of ' + items.length + ' results';
      document.querySelectorAll('.tab-btn').forEach(function (b) {
        b.classList.toggle('active', b.getAttribute('data-tab') === tab);
      });
    }

    tabStrip.addEventListener('click', function (e) {
      var btn = e.target.closest('.tab-btn');
      if (!btn) return;
      var tab = btn.getAttribute('data-tab');
      window.location.hash = tab === 'all' ? '' : tab;
      applyFilter(tab);
    });

    var initial = window.location.hash.replace('#', '') || 'all';
    applyFilter(initial);
  }
});
