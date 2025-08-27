# Timecode Adjustment for Subtitle Files

一个用于调整字幕文件时间轴的Python工具，支持SRT和VTT格式字幕文件的整体时间轴前后移动。

A Python tool for adjusting subtitle file timecodes, supporting overall timeline shifting for both SRT and VTT format subtitle files.

## 功能特性 / Features

- 支持SRT和VTT格式字幕文件 / Support for SRT and VTT format subtitle files
- 整体时间轴前后移动 / Overall timeline forward/backward shifting
- 自动处理时间格式转换 / Automatic time format conversion
- 防止负时间处理 / Negative time prevention handling
- UTF-8编码支持 / UTF-8 encoding support

## 使用方法 / Usage

### 直接运行 / Direct Execution

```bash
python timeMove时间轴移动.py
```

运行后程序会提示：
1. 输入字幕文件路径
2. 输入时间移动数值（秒）
   - 正数：向后移动时间轴
   - 负数：向前移动时间轴

After running, the program will prompt for:
1. Subtitle file path
2. Time shift value (in seconds)
   - Positive number: shift timeline backward
   - Negative number: shift timeline forward

### 函数调用 / Function Call

```python
from timeMove时间轴移动 import shift_subtitle_timeline

# 调用函数
shift_subtitle_timeline("path/to/your/subtitle.srt", 5.5)
```

参数说明 / Parameters:
- `input_subtitle_path`: 字幕文件路径，设为0时会提示用户输入 / Subtitle file path, set to 0 for user input prompt
- `shift_second`: 移动秒数，设为0时会提示用户输入 / Shift seconds, set to 0 for user input prompt

## 支持格式 / Supported Formats

### SRT格式 / SRT Format
```
1
00:00:01,000 --> 00:00:03,000
Hello World
```

### VTT格式 / VTT Format
```
WEBVTT

1
00:00:01.000 --> 00:00:03.000
Hello World
```

## 注意事项 / Notes

- 程序会直接修改原字幕文件，建议先备份 / The program modifies the original subtitle file directly, backup recommended
- 当移动后的开始时间为负数时，会自动设置为00:00:00 / When the shifted start time becomes negative, it will be automatically set to 00:00:00
- 支持小数秒输入，如1.5秒 / Supports decimal seconds input, e.g., 1.5 seconds

## 系统要求 / System Requirements

- Python 3.x
- 标准库模块：re, subprocess / Standard library modules: re, subprocess

## 许可证 / License

本项目采用开源许可证，欢迎贡献代码。

This project is open source, contributions are welcome.
