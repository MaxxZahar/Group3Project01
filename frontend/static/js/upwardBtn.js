(function() {
  'use strict';
  function trackScroll() {
    var scrolled = window.pageYOffset;
    var coords = document.documentElement.clientHeight;

    if (scrolled > coords) {
      goTopBtn.classList.add('showupwardbtn');
    }
    if (scrolled < coords) {
      goTopBtn.classList.remove('showupwardbtn');
    }
  }

  function backToTop() {
    if (window.pageYOffset > 0) {
      window.scrollBy(0, -100);
      setTimeout(backToTop, 0);
    }
  }

  var goTopBtn = document.querySelector('.upward-btn');

  window.addEventListener('scroll', trackScroll);
  goTopBtn.addEventListener('click', backToTop);
})();