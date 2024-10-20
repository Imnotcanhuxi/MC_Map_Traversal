def check(
    start: str, mode: int, arg1: str, arg2: str | None = None
) -> str:
    if start == "":
        return "请先输入地图画的编号!"
    elif not start.isnumeric():
        return "请输入正确的地图画编号!"
    elif start := int(start) < 0:
        return "地图画编号不得为负!"

    if mode == 1:
        pass
    elif mode == 2:
        pass
    elif mode == 3:
        pass
    else:
        raise ValueError("mode:int")
