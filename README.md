# codingnirvana.in

Personal site of Rajesh Muppalla. It is a plain Jekyll site. GitHub Pages builds it on every push to `main`. There is no build step to set up.

## Write a post

1. Add a file to `_posts/` named `YYYY-MM-DD-short-title.md`.
2. Start it with this front matter:

   ```markdown
   ---
   title: "My post title"
   topic: ai
   ---

   Text in Markdown.
   ```

3. Commit and push. The post is live in about a minute.

You can do this from the browser. On github.com, open `_posts/`, click **Add file**, then **Create new file**. Or press `.` on the repo page to open the web editor.

Topic keys: `ai`, `boardgames`, `photography`, `badminton`, `quizzing`, `indix`. A post without a topic still shows on the home page and on `/writing/`.

## Drafts

Put unfinished posts in `_drafts/` with no date in the file name. Drafts are not published. To publish one, move it to `_posts/` and add the date to the file name. You can also keep a post in `_posts/` and add `published: false` to its front matter.

## Images

Put images in `assets/img/` and link them as `![alt text](/assets/img/name.jpg)`.

## Add a topic

1. Add an entry under `topics` in `_config.yml`.
2. Copy `badminton.md`, then change `title`, `topic` and `permalink`.

## Preview locally

```sh
bundle install
bundle exec jekyll serve --drafts
```

Then open http://localhost:4000. `--drafts` also shows the posts in `_drafts/`.

## Photography

The photo gallery is a separate repo, [codingnirvana/photography](https://github.com/codingnirvana/photography). GitHub serves it at https://www.codingnirvana.in/photography/.

## Board game collection

The list on `/boardgames/` comes from `_data/boardgames.yml`. A GitHub Action (`.github/workflows/bgg-sync.yml`) rewrites that file every Monday from the owned games in the BoardGameGeek collection of `codingnirvana`, and commits it if anything changed. To sync now, open the **Actions** tab, pick **Sync board games from BGG**, and click **Run workflow**.

The Action reads the BGG token from the repo secret `BGG_API_TOKEN`. To run the sync locally:

```sh
BGG_API_TOKEN=... python3 scripts/bgg_sync.py
```
