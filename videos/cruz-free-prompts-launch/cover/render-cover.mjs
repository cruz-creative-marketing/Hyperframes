// Render cover/cover.html to cover/cover.png at 1080×1920.
// Run from the project root: NODE_PATH="$(npm root -g)" node cover/render-cover.mjs
import { createRequire } from "node:module";
import { fileURLToPath, pathToFileURL } from "node:url";
import { dirname, join } from "node:path";

const require = createRequire(import.meta.url);
const { chromium } = require("playwright");
const here = dirname(fileURLToPath(import.meta.url));

const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: 1 });
await page.goto(pathToFileURL(join(here, "cover.html")).href);
await page.evaluate(() => document.fonts.ready);
await page.waitForLoadState("networkidle");
await page.screenshot({ path: join(here, "cover.png"), type: "png" });
await browser.close();
console.log("wrote", join(here, "cover.png"));
