# CSV 到 iCal 转换器

这是一个简单的 Python 脚本,用于将 CSV 格式的任务或事件数据转换为 iCal (.ics) 格式。

## 功能

- 将 CSV 文件中的任务/事件数据转换为 iCal 格式
- 支持多种事件属性,包括:
  - 标题
  - 描述
  - 开始时间
  - 结束时间
  - 持续时间
  - 状态
  - 优先级
  - 标签
  - 链接
  - 父任务
  - 项目负责人
  - 团队

## 使用方法

1. 确保已安装所需的依赖:
   ```
   pip install icalendar
   ```

2. 准备您的 CSV 文件,确保包含必要的列(至少需要 "Label" 和 "Start Date")。

3. 在脚本中修改输入和输出文件名:
   ```python
   csv_to_ical('input.csv', 'output.ics')
   ```

4. 运行脚本:
   ```
   python ical.py
   ```

## CSV 文件格式

CSV 文件应包含以下列(部分可选):

- Label (必需): 事件标题
- Start Date (必需): 开始日期和时间 (格式: YYYY-MM-DD HH:MM)
- End Date (可选): 结束日期和时间 (格式: YYYY-MM-DD HH:MM)
- Duration (可选): 持续时间 (例如: "2 hours, 30 minutes")
- Summary (可选): 事件描述
- Status (可选): 事件状态
- Priority (可选): 优先级 (High, Normal, Low)
- Tags (可选): 标签 (逗号分隔)
- Links (可选): 相关链接
- Parent (可选): 父任务 ID
- Project Lead (可选): 项目负责人
- Team (可选): 团队名称

## 注意事项

- 日期时间格式必须为 "YYYY-MM-DD HH:MM"
- 如果未提供结束日期,脚本将使用开始日期加上持续时间(如果提供)
- 优先级会被映射为 iCal 的数字优先级 (1: 高, 5: 正常, 9: 低)

## 贡献

欢迎提交问题和拉取请求来改进这个项目。

## 许可

[MIT License](LICENSE)
