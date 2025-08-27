def shift_subtitle_timeline(input_subtitle_path, shift_second):
    import subprocess
    import re
    # 输入字幕路径
    if input_subtitle_path == 0:
        input_subtitle_path = input('请输入字幕文件路径：').replace('"', '')
    input_subtitle_name = input_subtitle_path.split('\\')[-1]
    input_subtitle_format = input_subtitle_name.split('.')[-1]
    # 确认字幕移动时间数值
    if shift_second == 0:
        shift_second = float(input('请输字幕时间线移动数值，正整数为向后移动，负整数为向前移：'))
    # 获取字幕内容
    with open(input_subtitle_path, 'r', encoding='UTF-8') as f:
        subtitle_data = f.readlines()
    # 提取时间点并修改
    for line in subtitle_data:
        if '-->' in line:
            where = subtitle_data.index(line)  # 标记索引
            line = line.replace('\n', '')  # 去掉换行符
            start, end = line.split(' --> ')  # 开始结束时间
            start_h, start_m, start_s, start_ms = re.split(r'[:,.]', start)  # 开始时间
            end_h, end_m, end_s, end_ms = re.split(r'[:,.]', end)  # 结束时间
            start_total_ms = int(start_h) * 3600000 + int(start_m) * 60000 + int(start_s) * 1000 + int(start_ms)
            end_total_ms = int(end_h) * 3600000 + int(end_m) * 60000 + int(end_s) * 1000 + int(end_ms)
            shift_second_ms = int(shift_second * 1000)  # 将移动时间换算成毫秒，加上int确保取整，不留.0，以防止后面的02d方法报错。
            start_total_ms = start_total_ms + shift_second_ms  # 添加了移动时间的开始时间
            if start_total_ms < 0:  # 如果开始时间变为负数，将其设为0
                start_total_ms = 0
            else:
                end_total_ms = end_total_ms + shift_second_ms  # 添加了移动时间的结束时间
            start_h, remain = divmod(start_total_ms, 3600000)  # 将开始时间转回时、分、秒、毫秒
            start_m, remain = divmod(remain, 60000)
            start_s, remain = divmod(remain, 1000)
            start_ms = remain
            end_h, remain = divmod(end_total_ms, 3600000)  # 将开始时间转回时、分、秒、毫秒
            end_m, remain = divmod(remain, 60000)
            end_s, remain = divmod(remain, 1000)
            end_ms = remain
            if input_subtitle_format == 'srt':
                start = f'{start_h:02d}:{start_m:02d}:{start_s:02d},{start_ms:03d}'
                end = f'{end_h:02d}:{end_m:02d}:{end_s:02d},{end_ms:03d}'  # 将结束时间换回00:00:00,000格式
            elif input_subtitle_format == 'vtt':
                start = f'{start_h:02d}:{start_m:02d}:{start_s:02d}.{start_ms:03d}'
                end = f'{end_h:02d}:{end_m:02d}:{end_s:02d}.{end_ms:03d}'  # 将结束时间换回00:00:00,000格式
            line = start + ' --> ' + end + '\n'
            subtitle_data[where] = line
    # 清空字幕原有内容
    with open(input_subtitle_path, 'w', encoding='UTF-8') as f:
        f.write('')
    # 输入转换后的字幕内容
    with open(input_subtitle_path, 'a', encoding='UTF-8') as f:
        for line in subtitle_data:
            f.write(line)

shift_subtitle_timeline(0,0)
