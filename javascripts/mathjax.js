// MathJax 3 config for MkDocs Material + pymdownx.arithmatex (generic mode).
// arithmatex emits \( \) inline and \[ \] display inside .arithmatex spans/divs.
window.MathJax = {
  tex: {
    inlineMath: [["\\(", "\\)"], ["$", "$"]],
    displayMath: [["\\[", "\\]"], ["$$", "$$"]],
    processEscapes: true,
    processEnvironments: true
  },
  options: {
    ignoreHtmlClass: ".*|",
    processHtmlClass: "arithmatex"
  }
};

// Re-typeset after Material's instant navigation swaps page content.
// (Plain typesetPromise() is idempotent and safe; do NOT call typesetClear()
//  or reset document state here — that blanks the math on first load.)
document$.subscribe(() => {
  MathJax.typesetPromise();
});
