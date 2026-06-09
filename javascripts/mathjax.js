// MathJax 3 config for MkDocs Material + pymdownx.arithmatex (generic mode)
window.MathJax = {
  tex: {
    inlineMath: [["$", "$"], ["\\(", "\\)"]],
    displayMath: [["$$", "$$"], ["\\[", "\\]"]],
    processEscapes: true,
    processEnvironments: true
  },
  options: {
    ignoreHtmlClass: ".*|",
    processHtmlClass: "arithmatex"
  }
};

// Re-typeset on Material's instant (SPA-style) navigation
document$.subscribe(() => {
  if (window.MathJax && MathJax.typesetPromise) {
    MathJax.startup.document.state(0);
    MathJax.texReset();
    MathJax.typesetClear();
    MathJax.typesetPromise();
  }
});
