パチイベNAVI 公開データ連携アップデート

GitHub リポジトリのルートへ index.html, sw.js, events.json, update_events.py をアップロードし、.github/workflows/check-events.yml を同じパスで作成してください。manifest.webmanifest と icon.svg は既存のものをそのまま使用します。

events.json の events 配列へ確認済みの情報を追加すると、全利用者のアプリに反映されます。例:
{"updated_at":"2026-10-21","events":[{"shop":"店舗名","pref":"奈良県","city":"橿原市","date":"2026-10-22","type":"来店","detail":"告知内容","source":"https://example.com/official-event","confidence":"公式確認"}]}
上記は構造説明用の架空例で、実在イベントではありません。updated_at は実際に情報を確認した日付にしてください。

GitHub Actions は毎朝7:15 JSTにJSONの形式を検証するだけです。外部サイトからの自動収集は行いません。取得先の許可/API仕様を確認してから別途実装が必要です。
