# ID 工具包

![version-2.1.0](https://img.shields.io/badge/version-2.1.0-blue)

## 引入模块

```python
import idtool
```

## 构造参数

### idtool.IDGenerator

- `length: int = None`

    等宽 ID 字符位数。为空表示不限制位数。

- `chars: typing.Sequence = None`

    ID 字符序列（例如 ['1', '2', '3'] ）。默认值为 ['0', '1', ..., '9', 'a', 'b', ..., 'z']。

- `initial: str = None`

    初始 ID。

## 接口说明

### idtool.IDGenerator

- `idtool.IDGenerator.next() -> bool`

    生成下一个 ID 并返回是否有进位。

- `idtool.IDGenerator.get_id() -> str`

    返回当前 ID。

- `idtool.IDGenerator.set_id(new_id: str)`

    设置当前 ID。

### idtool.IDManager

- `idtool.IDManager.add_id(generator: idtool.IDGenerator, auto_increase: bool = False)`

    给 ID 管理器添加一个 ID 。 `auto_increase` 代表该位是否会由于低位进位而自动增长。

- `idtool.IDManager.add_separator(separator: str)`

    给 ID 管理器添加一个 str 作为分隔符。

- `idtool.IDManager.next(index: int = None)`

    对指定位置的 ID 进行进位。

- `idtool.IDManager.set_id(index: int, new_id: str)`

    更改指定位置的 ID。

- `idtool.IDManager.get_id() -> str`

    返回当前 ID。

## 异常

- `idtool.IDGenerator.DuplicateChars`

    字符序列存在重复字符。

- `idtool.IDGenerator.IllegalIDFormat`

    要设置的 ID 格式不正确。
