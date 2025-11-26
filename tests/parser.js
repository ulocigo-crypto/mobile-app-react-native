import { parse as parseHTML } from 'node-html-parser';
import { parse as parseCSS } from 'css-parse';

const parseHtml = (html) => {
  try {
    return parseHTML(html);
  } catch (error) {
    throw new Error(`Failed to parse HTML: ${error}`);
  }
};

const parseCss = (css) => {
  try {
    return parseCSS(css);
  } catch (error) {
    throw new Error(`Failed to parse CSS: ${error}`);
  }
};

export { parseHtml, parseCss };