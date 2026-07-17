class box:
    def __init__(self, name: str, weight: float, height: float, width: float, priority: int):
        self.name = name
        self.weight = weight
        self.height = height
        self.width = width
        self.priority = priority
    def __repr__(self):
        return f"{self.name} (wt: {self.weight}lb, ht: {self.height}in, wd: {self.width}in, pr: {self.priority})"

factory_line = [
    box("First!", weight=45.7, height=56.8, width=130.1, priority=2),
    box("Tungsten (probably)", weight=3451.1, height=555.5, width=555.5, priority=1),
    box("IMPORTANT (FRAGILE)", weight=11.5, height=3.2, width=5.6, priority=3)
]

prio_config = {
    "height_i": 0.05,
    "width_i": 0.05,
    "weight_i": 0.25,
    "priority_i": 0.65
}

def calc_score(box, config):
    calc = (box.height * config["height_i"]) + (box.width * config["width_i"]) + (box.weight * config["weight_i"]) + (box.priority * config["priority_i"])
    return calc

sorted_line = sorted(
    factory_line,
    key=lambda box: calc_score(box, prio_config),
    reverse=True
)

print(sorted_line)
