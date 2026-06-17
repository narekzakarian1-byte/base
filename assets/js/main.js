/* HEXAGON CONSULTING — interactions */
(function () {
  "use strict";

  /* ---- Navbar shadow on scroll ---- */
  var nav = document.querySelector(".nav");
  var onScroll = function () {
    if (!nav) return;
    nav.classList.toggle("scrolled", window.scrollY > 24);
  };
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  /* ---- Mobile drawer ---- */
  var toggle = document.querySelector(".nav-toggle");
  var drawer = document.querySelector(".drawer");
  var closeBtn = document.querySelector(".drawer-close");
  var openDrawer = function () { if (drawer) { drawer.classList.add("open"); document.body.style.overflow = "hidden"; } };
  var closeDrawer = function () { if (drawer) { drawer.classList.remove("open"); document.body.style.overflow = ""; } };
  if (toggle) toggle.addEventListener("click", openDrawer);
  if (closeBtn) closeBtn.addEventListener("click", closeDrawer);
  if (drawer) drawer.querySelectorAll("a").forEach(function (a) { a.addEventListener("click", closeDrawer); });

  /* ---- Scroll reveal ---- */
  var reveals = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window && reveals.length) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); }
      });
    }, { threshold: 0.12, rootMargin: "0px 0px -8% 0px" });
    reveals.forEach(function (el) { io.observe(el); });
  } else {
    reveals.forEach(function (el) { el.classList.add("in"); });
  }

  /* ---- Animate the growth chart stroke when visible ---- */
  var chart = document.querySelector("[data-chart-path]");
  if (chart && "IntersectionObserver" in window) {
    var len = chart.getTotalLength ? chart.getTotalLength() : 1000;
    chart.style.strokeDasharray = len;
    chart.style.strokeDashoffset = len;
    var cIo = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) {
          chart.style.transition = "stroke-dashoffset 2.2s cubic-bezier(0.22,1,0.36,1)";
          chart.style.strokeDashoffset = "0";
          cIo.unobserve(e.target);
        }
      });
    }, { threshold: 0.4 });
    cIo.observe(chart);
  }

  /* ---- Smooth anchor offset for fixed nav ---- */
  document.querySelectorAll('a[href^="#"]').forEach(function (link) {
    link.addEventListener("click", function (ev) {
      var id = link.getAttribute("href");
      if (id.length < 2) return;
      var target = document.querySelector(id);
      if (!target) return;
      ev.preventDefault();
      var y = target.getBoundingClientRect().top + window.scrollY - 96;
      window.scrollTo({ top: y, behavior: "smooth" });
    });
  });

  /* ---- Current year ---- */
  var yr = document.querySelector("[data-year]");
  if (yr) yr.textContent = new Date().getFullYear();
})();
