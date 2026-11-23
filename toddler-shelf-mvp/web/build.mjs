import {mkdir,readFile,writeFile} from "node:fs/promises";
const html=await readFile("index.html","utf8");
const catalog=JSON.parse(await readFile("catalog.json","utf8"));
const photo=await readFile("demo.jpg");
const worker=await readFile("worker.mjs","utf8");
await mkdir("dist/server",{recursive:true});
await writeFile("dist/server/index.js",
  "const HTML="+JSON.stringify(html)+";\nconst CATALOG="+JSON.stringify(catalog)+";\nconst DEMO_JPEG="+JSON.stringify(photo.toString("base64"))+";\n"+worker);
