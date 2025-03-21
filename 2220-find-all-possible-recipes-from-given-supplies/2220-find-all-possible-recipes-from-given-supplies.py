class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        supplies_set = set(supplies)
        recipe_set = set(recipes)
        ingredient_to_recipes = defaultdict(list)
        indegree = {}
        
        # Initialize indegree for all recipes
        for recipe, ingredient_list in zip(recipes, ingredients):
            if recipe in supplies_set:
                indegree[recipe] = 0
            else:
                required = 0
                for ingredient in ingredient_list:
                    if ingredient in supplies_set:
                        continue
                    if ingredient in recipe_set:
                        ingredient_to_recipes[ingredient].append(recipe)
                        required += 1
                    else:
                        required += 1
                indegree[recipe] = required
        
        queue = deque(supplies)  # Start with all supplies
        # Add recipes with zero indegree not in supplies
        for recipe in recipes:
            if indegree[recipe] == 0 and recipe not in supplies_set:
                queue.append(recipe)
        
        result = []
        while queue:
            current = queue.popleft()
            # Add to result if current is a recipe
            if current in recipe_set:
                result.append(current)
            # Process dependent recipes
            for neighbor in ingredient_to_recipes.get(current, []):
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        return result