# ID 工具包

项目基于 [Python](https://www.python.org/) 制作。

# 说明

## 引入模块

```python
import id_toolkit
```

## 构造参数

### IDGenerator

- `length`

    一个 int ，代表 ID 字符位数。

- `chars=None`

    一个无重复字符列表，代表 ID 字符序列（例如 ['1', '2', '3'] ）。默认值为 ['0', '1', ..., '9', 'a', 'b', ..., 'z'] 。

- `initial=None`

    一个字符串，代表初始 ID。

## 接口说明

### IDGenerator

- `id_toolkit.IDGenerator.next()`

    生成并返回下一个 ID。

- `id_toolkit.IDGenerator.get_id()`

    返回当前 ID。

- `id_toolkit.IDGenerator.set_id(new_id)`

    设置当前 ID。

### IDManager

- `id_toolkit.IDManager.add_id(length, chars=None, initial=None, auto_increase=False)`

    给 ID 管理器添加一个 ID 。 `length` / `chars` / `initial` 的定义与 `IDGenerator` 中的一样， `auto_increase` 代表该位是否会由于低位进位而自动增长。

- `id_toolkit.IDManager.add_separator(separator)`

    给 ID 管理器添加一个 str 作为分隔符。

- `id_toolkit.IDManager.next(index=None)`

    对指定位置的 ID 进行进位。

- `id_toolkit.IDManager.set_id(index, new_id)`

    更改指定位置的 ID。

- `id_toolkit.IDManager.get_id()`

    返回当前 ID。

## 异常

- `id_toolkit.IDGenerator.DuplicateChars`

    字符序列存在重复字符。

- `id_toolkit.IDGenerator.IllegalIDFormat`

    要设置的 ID 格式不正确。
