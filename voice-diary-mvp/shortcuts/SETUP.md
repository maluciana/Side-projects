# iPhone 快捷指令设置

先手动运行几天，确认“今日筛选、转录、生成、保存”都正确，再加定时自动化。

## 建议动作顺序

1. **Find Voice Recording**：筛选创建日期为今天；按创建日期升序。
2. **If**：没有录音时，创建当天标题和“今天没有 Voice Memo 记录。”。
3. **Repeat with Each**：对每条录音执行 **Transcribe Audio**，并把录音标题/创建时间与转录文本一起累积成文本。若动作输出没有时间，写“时间未注明”。
4. **Use Model**：选择可用的 Apple Intelligence 模型或 ChatGPT；粘贴 [`../prompts/organize-zh.md`](../prompts/organize-zh.md) 的指令，并把累积的转录文本作为输入。
5. **Save File**：保存模型输出到 Obsidian vault 的 `Daily Voice Diary/YYYY-MM-DD.md`。初期可开启“询问保存位置”，确认路径后再关闭。
6. 若当天重复运行可能覆盖文件，先选择“询问是否替换”，或把当天所有结果先合并后只保存一次。

> iOS 对 Shortcuts 的动作名称、可用过滤条件和自动运行要求会随系统版本变化。先在动作搜索中确认 `Find Voice Recording`、`Transcribe Audio`、`Use Model` 可用，并手动验证当天筛选结果。若录音动作不能返回转录文本或文件，保留同一条目格式，先从 Voice Memos 选中当天录音并通过分享表单运行这个整理流程。

## 每晚自动运行

验证手动快捷指令后，在 Shortcuts → Automation 建立每天晚上运行的 Time of Day 自动化，并选择刚创建的快捷指令。若系统要求确认运行，先保留确认，观察几天后再调整。

## 隐私建议

- 日记 Markdown 放在自己的 Obsidian vault，不要提交到 GitHub。
- 尽量在本机完成语音转录；如果 `Use Model` 把转录文本发往云端模型，按该模型的隐私设置决定是否使用。
- 不要把原始录音、转录文本或真实日记样例放进这个代码仓库。
