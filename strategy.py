class SpacesModificationStrategy:
    def modify(self, inp):
        pass


class DoubleSpacesStrategy(SpacesModificationStrategy):
    def modify(self, inp):
        return inp.replace(" ", "  ")


class RemoveSpacesStrategy(SpacesModificationStrategy):
    def modify(self, inp):
        return inp.replace(" ", "")


class ReplaceWithUnderscoreStrategy(SpacesModificationStrategy):
    def modify(self, inp):
        return inp.replace(" ", "_")


class SpaceModificationStrategyProvider:
    def get(self, strategy_type):
        if strategy_type == "double":
            return DoubleSpacesStrategy()
        elif strategy_type == "remove":
            return RemoveSpacesStrategy()
        elif strategy_type == "replace":
            return ReplaceWithUnderscoreStrategy()


strategy_type = input("Chose a strategy [doubole|remove|replace]: ")
inp = "Hello this is SDA class!"

strategy = SpaceModificationStrategyProvider().get(strategy_type)
output = strategy.modify(inp)

print(output)
