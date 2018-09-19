# ID 序列生成器

项目基于 [Python](https://www.python.org/) 语言制作。

# 说明

## 引入模块

```python
from id_generator import IDGenerator
```

## 构造参数

- `length`

    一个 int ，代表 ID 字符位数

- `chars`

    一个无重复字符列表，代表 ID 字符序列（例如 ['1', '2', '3'] ）

- `initial`

    一个字符串，代表初始 ID
## 接口说明

- `next()`

    生成并返回下一个 ID

- `get_id()`

    返回当前 ID

- `set_id(new_id)`

    设置当前 ID

## 异常

- `DuplicateChars`

    字符序列存在重复字符

- `IllegalIDFormat`

    要设置的 ID 格式不正确

- `IDOutOfRange`

    ID 超出范围
