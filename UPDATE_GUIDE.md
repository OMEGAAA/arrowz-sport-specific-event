# 競技特化イベント LP — 更新・変更マニュアル

このランディングページ（`index.html`）を、シリーズの新しい回（第3弾、第4弾…）や別テーマで再利用するためのマニュアルです。

---

## 0. 前提

- 本 LP はシングル HTML ファイル（`index.html`）のみで構成。CSS・JS もファイル内に同梱済み。
- 画像はすべてリポジトリ直下（`index.html` と同じ階層）にフラット配置。
- 外部依存は Google Fonts のみ。
- ブラウザで `index.html` を直接開けば表示確認可能（サーバー不要）。

> ⚠️ **GitHub Pages で画像が出ない時のチェック（重要）**
> - **ファイル名・フォルダ名は必ず半角英数字**（例: `booking-1.jpeg`、`coach-kawai.jpg`）。`予約①.jpeg` や `スクリーンショット....png` のような**全角・日本語・丸数字・スペース**は NG。Windows/OneDrive では Unicode 正規化の違いで git のパスと HTML 参照がズレて 404 になる。
> - 拡張子の**大文字小文字も一致**させる（`.JPG` と `.jpg` は別物扱い）。
> - 画像を追加する時は、**先に ASCII 名にリネームしてから**コミット → `git push`。
>
> ⚠️ **画像サイズ（アップロード失敗の主因）**
> - GitHub Web UI（ブラウザでドラッグ＆ドロップ）は **1 ファイル 25MB** が上限。iPhone 等のオリジナル写真（10MB超）はそのまま上げるとはじかれる。
> - 目安: 写真 1 枚 **1MB 以下**、最大辺 **1920px**、JPEG 品質 **80〜85**。
> - 圧縮方法: [TinyJPG](https://tinyjpg.com) や [Squoosh](https://squoosh.app) にドラッグで縮小 → ダウンロード → 元ファイルを差し替え。
>
> ⚠️ **GitHub Web UI はフォルダ構造を潰す**
> - ブラウザで `images/` フォルダの**中身を選んでドラッグ**すると、フォルダが消えて全ファイルがリポジトリ直下に置かれる。
> - このため本 LP は **フラット構造**（全ファイルをリポジトリ直下）を採用。HTML 側も `src="IMG_4868.jpg"` のように**フォルダ prefix なし**で書いている。
> - アップロード時は**全ファイルを直下に**配置したままドラッグすれば OK。

### ディレクトリ構造（フラット配置）

GitHub Web UI のアップロードはサブフォルダが潰れるため、**全ファイルをリポジトリ直下に配置**しています。

```
競技特化イベント/
├── index.html           ← 本体ファイル
├── UPDATE_GUIDE.md      ← このマニュアル
├── coach-kawai.jpg      コーチ顔写真
├── coach-okubo.jpg      コーチ顔写真
├── IMG_48xx.jpg         セッション写真（ヒーロー背景・ギャラリー・ドリル）
├── flyer-1.png          公式フライヤー表
├── flyer-2.png          公式フライヤー裏
├── booking-1.jpeg       予約ステップ 1
├── booking-2.png        予約ステップ 2
├── booking-3.png        予約ステップ 3
└── booking-4.png        予約ステップ 4
```

---

## 1. よくある更新（Quick Reference）

次の回で差し替えることが多い項目を一覧化。行番号は現状の `index.html` 基準。

| 項目 | 場所（行） | 備考 |
|---|---|---|
| ページタイトル（ブラウザのタブ） | 7 行目 `<title>` | |
| SEO description | 8 行目 `<meta name="description">` | |
| 開催日 (JS カウントダウン) | 約 3133 行目 `new Date('2026-05-10T14:00:00+09:00')` | ISO 形式・日本時間 |
| ヒーロー背景写真（4枚ループ） | 2518〜2521 行目 `.hero-slide` | 4枚必須 |
| 予約 URL（ナビ・CTA 2箇所） | 約 2510 行目・3068 行目 | 同じ URL を2箇所に記載 |
| 開催日表示（5.10 SUN/MAY） | 2536〜2537 行目 `.date-en` `.big` | |
| 料金 | 約 2902 行目 `¥4,950` | |
| 定員・時間帯・会場 | 2882〜2929 行目 `.detail-grid` | |
| コーチ情報 | 2766〜2812 行目 `.coach` | |

---

## 2. セクション別・更新ガイド

LP は HTML コメント `<!-- =============== XXX =============== -->` でセクション分けされています。Ctrl+F で検索できます。

### 2-1. NAV（ナビゲーション）— 約 2491 行目

- 左のブランド表示：`<small>ARROWS × AGEKKE</small>` と `<strong>競技特化 / 02</strong>`。シリーズ番号を更新。
- ナビリンク：全てページ内アンカー（`#concept` 等）。セクションを削除したら対応するリンクも外す。
- 右の「参加申込」ボタン：予約サイトの URL。**CTA セクションの URL と必ず一致させる**。

### 2-2. HERO（ファーストビュー）— 約 2515 行目

```html
<div class="hero-slides" aria-hidden="true">
  <div class="hero-slide" style="background-image:url('IMG_4868.jpg')"></div>
  <div class="hero-slide" style="background-image:url('IMG_4874.jpg')"></div>
  <div class="hero-slide" style="background-image:url('IMG_4883.jpg')"></div>
  <div class="hero-slide" style="background-image:url('IMG_4891.jpg')"></div>
</div>
```

- **背景写真ループ**：4 枚で 1 サイクル（24 秒）。`.hero-slide` を増減させる場合、CSS の `animation-delay`（行 349〜352）と `@keyframes heroSlideLoop` のタイミングを再計算する。枚数維持が最も簡単。
- **メタ表記** `.hero-meta`（2528〜2532 行目）：`COMPETITION-SPECIFIC TRAINING / VOL.02` のバージョン、会場名などを更新。
- **カウントダウン表示**（2536〜2538 行目）：
  - `SUN / MAY` → 曜日/月
  - `5.10` → 日付
  - `開催まであと` → 固定
- **章番号 / タイトル**（2548〜2549 行目）：`02` と `VOLUME TWO / BASE-RUNNING EDITION` を更新。
- **ヒーロータイトル `<h1>`**（2552〜2558 行目）：
  ```
  RUN FAST, STEAL / FASTER.
  ```
  装飾用のスパン（`.gold` `.outline` `.red` `.slash`）を使って色分けしている。英単語 2〜3語 × 2行が視覚バランスに最適。
- **日本語キャッチ `.hero-jp`**（2560〜2563 行目）：`競技特化トレーニング 野球走塁編。` を差し替え。
- **ヒーロー下部**（2565〜2580 行目）：リード文、セッション時間、コーチ人数。

### 2-3. TICKER（流れるテキスト）— 約 2584 行目

```html
<span>BASE RUNNING <i></i> 0.01sec FASTER <i></i> ...</span>
```

- 同じ `<span>` を 2 個並べて無限スクロール。**2つは必ず同じ内容** にする（シームレスに繋ぐため）。
- キーワードは `<i></i>`（ドット装飾）で区切る。

### 2-4. CONCEPT — 約 2595 行目

- 透かし文字（背景の巨大英字）：`.concept-ghost` → `VELOCITY` を変更（2596 行目）。
- 引用風キャッチ `.concept-quote`（2605〜2610 行目）：3 行構成が見やすい。
- 本文 `.concept-text`（2611〜2622 行目）：2 段落構成。コーチ名を `<strong>` でハイライト。

### 2-5. PILLARS（3つの柱）— 約 2627 行目

- セクションタイトル（2635 行目）：`em` タグ内の英単語が黄色ハイライトされる。
- 3 つの `.pillar` カード（2639〜2653 行目）：番号 `→ 01` と見出し・本文の構造を維持。

### 2-6. TRAINING MENU — 約 2657 行目

- 見出しの大字（2667 行目）：`<em>90</em>MIN RUN&nbsp;LAB.` の数字部分は `em` で黄色ハイライト。
- `.drill` カード（2674〜2725 行目）：現状 2 枚。追加する場合は `<article class="drill reveal d2">` 等でディレイを追加。
  - 画像：`<img src="xxx.jpg" style="object-position: center 45%;">`。`object-position` で被写体の見せたい位置を調整。
  - `.drill-foot` 内の「強度: ●●●○○」は **全角文字で手動調整**。

### 2-7. PHOTOBAND（全幅の写真バンド）— 約 2730 行目

- 1 枚のフル幅写真 + 引用。`IMG_4877.jpg` を差し替えるだけ。
- `.big` の `0.01` は数値を変更可能。

### 2-8. COACHES — 約 2751 行目

各 `.coach` カード（2766〜2812 行目）の構造：

```html
<article class="coach reveal">
  <div class="coach-top">
    <div class="coach-avatar has-img">
      <img src="coach-xxx.jpg" alt="...">
    </div>
    <div>
      <div class="coach-name-jp">名前</div>
      <div class="coach-name-en">NAME &nbsp;/&nbsp; ROLE</div>
    </div>
  </div>
  <div class="coach-role">ROLE TAGLINE（英）</div>
  <p class="coach-bio">経歴文（和）</p>
  <div class="coach-tags">
    <span class="coach-tag">タグ1</span>
    <span class="coach-tag">タグ2</span>
  </div>
</article>
```

- **顔写真**：正方形推奨（600×600px 以上）。`object-position: center 25%` で顔位置調整（CSS 側 1207 行目）。
- **タグ数**：4個までが見栄えが良い。

### 2-9. GALLERY — 約 2818 行目

- 8 枚グリッド（`g1`〜`g8`）。クラス名 `.g1`〜`.g8` がそれぞれ異なるサイズを持つので、**順番は崩さない** こと。
- `data-caption="01 · Base running"` がホバー時の説明文。
- セクション見出し（2829 行目）`FIELD NOTES. 第一回の記録。` は「第◯回の記録」として回を更新。

### 2-10. DETAILS（開催概要）— 約 2868 行目

6 枚のタイル（日付・料金・定員・対象・会場 等）。それぞれ独立して編集可能。

- `.tile.t-date`：日付と 2部制の時間帯
- `.tile.t-price`：料金（赤背景）
- `.tile.t-size`：定員（黄背景）
- `.tile.t-age`：対象学年
- `.tile.t-venue`：会場と公式サイトリンク

### 2-11. HOW TO BOOK — 約 2935 行目

4 ステップの予約フロー。スクショ 4 枚（`booking-1.jpeg`〜`booking-4.png`）+ 説明文。**予約サイトの UI が変わったらスクショを撮り直す**（※ファイル名は ASCII 固定。日本語ファイル名で上書きしない）。

### 2-12. NOTES（注意事項）— 約 3005 行目

`<li>` の箇条書き。`<b style="color:var(--gold)">先着順</b>` のように重要語を黄色強調。

### 2-13. POSTER（公式フライヤー）— 約 3022 行目

`flyer-1.png`（表）と `flyer-2.png`（裏）の 2 枚。差し替えのみ。

### 2-14. CTA（最終申込ボタン）— 約 3053 行目

- 背景の大字 `.cta-ghost` → `BOOK NOW` を変更可能。
- 見出し `BE FASTER.`（3058〜3061 行目）と日本語 `一歩目を、変える。いま、申し込む。`。
- **予約 URL**（3068 行目）：**NAV の URL と同一** にする。
- 電話番号（3075 行目）`0282-25-8288` を更新。

### 2-15. FOOTER — 約 3082 行目

- Contact：電話番号・受付場所・Instagram URL
- Series：シリーズ一覧。次回を追加したら `Vol.03` の行を `NOW` に切り替える。
- Copyright の年号

---

## 3. カウントダウンタイマーの更新（重要）

最下部の `<script>` 内、約 3133 行目：

```js
const target = new Date('2026-05-10T14:00:00+09:00').getTime();
```

- ISO 8601 形式・日本時間（+09:00）で指定。
- 第1部の開始時刻に合わせるのが自然。
- 開催日を過ぎると自動的に `00 / 00 / 00 / 00` 表示になる。

---

## 4. デザイントークン（配色・フォント）— 約 61 行目

```css
:root {
  --ink: #0a0a0a;        /* 背景ブラック */
  --ink-2: #141414;
  --ink-3: #1e1e1e;
  --bone: #f3efe5;       /* オフホワイト（テキスト） */
  --bone-dim: #d5d0c4;
  --gold: #ffd60a;       /* アクセント黄（スタジアムライト） */
  --gold-deep: #e5be00;
  --crimson: #e4002b;    /* アクセント赤（野球色） */
  --crimson-dim: #b8001f;
}
```

**別テーマで再利用する場合は、この 8 色を差し替えるだけで全体トーンが変わる。** 例えばサッカー編なら緑系、バスケ編ならオレンジ系など。

### フォント（79〜82 行目）

- `--display-en`：Anton（ヒーローの英大字）
- `--display-ja`：Zen Kaku Gothic New（日本語見出し）
- `--mono`：JetBrains Mono（数字・英字ラベル）
- `--body`：Noto Sans JP（本文）

Google Fonts の import は 13 行目。フォントを変える場合は URL と `:root` の両方を更新。

---

## 5. 画像運用ルール

### 命名規則
- コーチ写真：`coach-{姓ローマ字}.jpg`
- セッション写真：元のファイル名（`IMG_xxxx.jpg`）のまま
- フライヤー：`flyer-1.png`（表）/ `flyer-2.png`（裏）

### サイズ目安
| 用途 | 推奨サイズ | 形式 |
|---|---|---|
| ヒーロー背景 | 横 1920px 以上 | JPG |
| コーチ顔写真 | 600×600px 以上 | JPG（顔中心） |
| ギャラリー | 横 1200px 以上 | JPG |
| フライヤー | そのまま高解像度 | PNG |
| 予約スクショ | スマホ実寸 | JPEG/PNG |

### 被写体位置調整
画像がトリミングされて顔や主要被写体が切れる場合、該当 `<img>` の style で調整：

```html
<img src="..." style="object-position: center 25%;">
```

値は 0%（上端）〜 100%（下端）。

---

## 6. 新しい回を作るときの標準手順

1. フォルダを複製（例：`競技特化イベント_vol03/`）。
2. 写真を新しいものに差し替え。**既存のファイル名を維持すると HTML 修正が最小限で済む**。
3. `index.html` を以下の順で更新：
   1. `<title>` / `<meta description>`
   2. NAV（シリーズ番号）
   3. HERO（タイトル・キャッチ・日付・章番号）
   4. CONCEPT / PILLARS（本文）
   5. TRAINING MENU（ドリル内容）
   6. COACHES（登場コーチ）
   7. DETAILS（日程・料金・会場）
   8. NOTES（注意事項）
   9. POSTER（フライヤー）
   10. CTA（予約 URL）
   11. FOOTER（シリーズ一覧を進める）
4. カウントダウンの target 日時（JS）を更新。
5. ブラウザで `index.html` を開いて全セクションを目視確認。
6. Chrome DevTools のモバイル表示（375×812px など）でも確認。

---

## 6.5. 表示モード切替ボタン（PC ⇄ スマホ）

画面右下に常時表示される丸いボタン。ユーザー自身で PC 版／スマホ版を切り替え可能。

**動作**
- 初回訪問：画面幅 820px 以下 → スマホ版、それ以上 → PC 版（自動判定）
- ボタン押下で反対のモードに切替。選択は `localStorage` に保存され次回以降も維持。
- スマホで「PC版で表示」→ viewport を `width=1280` に固定し、PC レイアウトを縮小表示。
- PC で「スマホ版で表示」→ body を 430px 幅に固定し、スマホ風フレームで疑似プレビュー。

**カスタマイズ場所（`index.html`）**
- 初期化スクリプト: `<head>` 内、viewport meta の直後
- スタイル: `.view-toggle` / `html.force-mobile` の CSS
- HTML とロジック: `</body>` 直前の `<button class="view-toggle">` と `<script>`

**非表示にしたい場合**：`<button class="view-toggle">` の行を削除、または CSS に `.view-toggle { display: none; }` を追加。

---

## 7. トラブルシューティング

| 症状 | 原因・対処 |
|---|---|
| ヒーロー背景が動かない | `prefers-reduced-motion: reduce` がOSで有効。意図通り。 |
| カウントダウンが `--` のまま | target 日時の形式が不正。ISO 8601 + タイムゾーン必須。 |
| 画像が表示されない | パスが大文字小文字違い・全角スペース混入・拡張子違い。 |
| フォントが崩れて表示される | ネットワーク不通で Google Fonts ロード失敗。フォールバックで表示されるので致命的ではない。 |
| スライドが重なって見える | `.hero-slide` を 5 枚以上に増やした場合、`animation-delay` と `@keyframes` のタイミング再計算が必要。 |
| スクロールでアニメーションしない要素がある | `class="reveal"` が付いていない、または `IntersectionObserver` 非対応の古いブラウザ。 |

---

## 8. 公開（デプロイ）

このファイルは静的 HTML なので、以下のいずれでも公開可能：

- **GitHub Pages** — リポジトリの Settings → Pages で有効化
- **Netlify / Vercel** — フォルダごとドラッグ&ドロップ
- **既存サイトのサブディレクトリ** — `index.html` と画像ファイルを FTP でアップロード

`<head>` の `canonical` や OGP タグ（SNS 共有用の画像・説明）を公開前に追加することを推奨。

---

## 9. 変更履歴メモ（このファイルに書き足す）

- 2026-04-22：初版作成（Vol.02 走塁編）
- 2026-04-23：ヒーロー背景の透明度調整、コーチカード余白調整、本マニュアル作成
