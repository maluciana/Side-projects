# Toddler Shelf mobile pilot

The pilot covers packaged yogurt for ages 12–23 months. The sample photo is [from Eat It Detroit](https://diningindetroita.blogspot.com/2011/08/eid-feature-whole-foods-is-really-not.html); its detection boxes are fixtures. The catalog includes sourced label records and a queue of unverified products. It does not establish local store inventory.

Run `node build.mjs` to create the hosted Worker. Configure the server-side secret `OPENAI_API_KEY` for live scanning. The model defaults to `gpt-5.4-nano`; set `OPENAI_MODEL=gpt-5.4-mini` to compare. The API calls OpenAI once per live photo and records token counts only. Profiles are stored in the browser, and only the photo goes to the model. The application server uses age and allergies to apply deterministic catalog rules.

Keep catalog changes in Git. Update the sources and check date when reviewing labels. Add confirmed new records and preserve unknown fields as null. Field-level evidence, multiple label versions, dedicated barcode confirmation, bread/snack data, and expanded retail coverage are follow-up work. This pilot uses a versioned JSON snapshot.

To reproduce the demo asset, save the shelf photo from the credited source as `demo.jpg` in this directory before running the build.
