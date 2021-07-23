const prettyMdPdf = require("pretty-markdown-pdf");

prettyMdPdf.convertMd({
  markdownFilePath: "./README.md",
  outputFilePath: "./book.pdf",
  stylesRelativePathFile: true,
  styles: ["./style.css"],
});
