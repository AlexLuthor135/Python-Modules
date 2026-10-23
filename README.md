# PYTHON_MODULES

A collection of Python exercises organized into modules, progressing from basic syntax and functions to object-oriented design, data processing, package management, validation, and functional programming.

Each module explores these concepts through a different setting: gardens, game analytics, digital archives, alchemy, creature battles, the Matrix, space missions, and spellcasting.

## Getting started

Use **Python 3.10 or newer**. Modules 00–07 and 10 use the Python standard library. Modules 08 and 09 require additional packages for some exercises.

```bash
git clone https://github.com/AlexLuthor135/Python-Modules.git
cd Python-Modules

python3 -m venv .venv
source .venv/bin/activate
```

On Windows, activate the environment with `.venv\Scripts\activate` instead.

Install the dependencies for the exercises you want to run:

```bash
# Module 08, Exercise 01: NumPy, pandas, and Matplotlib
python3 -m pip install -r python_module_08/ex1/requirements.txt

# Module 08, Exercise 02: python-dotenv
python3 -m pip install -r python_module_08/ex2/requirements.txt

# Module 09: Pydantic v2
python3 -m pip install "pydantic>=2,<3"
```

Most exercises include a demonstration that runs when the file is executed directly. For example, from the repository root:

```bash
python3 python_module_01/ex2/ft_plant_growth.py
python3 python_module_03/ex1/ft_score_analytics.py 100 250 75
python3 python_module_07/tournament.py
python3 python_module_10/ex4/decorator_mastery.py
```

Module 00 provides an interactive helper. Run it from its own directory so it can locate the exercise folders:

```bash
cd python_module_00
python3 main.py
```

The descriptions below follow the code currently included in this repository. Some demonstrations deliberately trigger errors to illustrate exception handling or import behavior.

## Modules

| Module | Main concepts | Directory |
| --- | --- | --- |
| 00 | Functions, input/output, conditions, loops, recursion, type hints | [python_module_00](python_module_00/) |
| 01 | Classes, constructors, encapsulation, inheritance, method types | [python_module_01](python_module_01/) |
| 02 | Exceptions, validation, custom errors, cleanup | [python_module_02](python_module_02/) |
| 03 | Command-line arguments, collections, generators, comprehensions | [python_module_03](python_module_03/) |
| 04 | File handling, standard streams, context managers | [python_module_04](python_module_04/) |
| 05 | Abstract classes, polymorphism, data streams, protocols | [python_module_05](python_module_05/) |
| 06 | Imports, packages, namespaces, circular dependencies | [python_module_06](python_module_06/) |
| 07 | Abstract factories, multiple inheritance, strategy pattern | [python_module_07](python_module_07/) |
| 08 | Virtual environments, dependencies, environment variables | [python_module_08](python_module_08/) |
| 09 | Pydantic models, constraints, enums, nested validation | [python_module_09](python_module_09/) |
| 10 | Lambdas, higher-order functions, closures, functools, decorators | [python_module_10](python_module_10/) |

---

<details>
<summary><strong>Python - Module 00: Growing Code</strong></summary>

Functions, variables, console input/output, arithmetic, conditional statements, iteration, recursion, and type hints.

<details>
<summary>Exercise 00: Hello Garden</summary>

[ft_hello_garden.py](python_module_00/ex0/ft_hello_garden.py) introduces function definitions and console output. Calling `ft_hello_garden()` prints a greeting to the garden community.

</details>

<details>
<summary>Exercise 01: Garden Name</summary>

[ft_garden_name.py](python_module_00/ex1/ft_garden_name.py) asks for a garden name and displays it with a status message. The exercise introduces user input, string variables, and formatted output.

</details>

<details>
<summary>Exercise 02: Plot Area</summary>

[ft_plot_area.py](python_module_00/ex2/ft_plot_area.py) reads a plot's length and width, converts both values to integers, and prints the calculated area. Invalid input is reported through an exception.

</details>

<details>
<summary>Exercise 03: Harvest Total</summary>

[ft_harvest_total.py](python_module_00/ex3/ft_harvest_total.py) collects three daily harvest values and adds them together. It combines repeated input, a list, and integer arithmetic.

</details>

<details>
<summary>Exercise 04: Plant Age</summary>

[ft_plant_age.py](python_module_00/ex4/ft_plant_age.py) checks a plant's age using an `if`/`else` statement. Plants older than 60 days are reported as ready to harvest; younger plants need more time.

</details>

<details>
<summary>Exercise 05: Water Reminder</summary>

[ft_water_reminder.py](python_module_00/ex5/ft_water_reminder.py) asks how many days have passed since the last watering. A conditional selects a watering reminder when the value is greater than two.

</details>

<details>
<summary>Exercise 06: Count to Harvest</summary>

Two implementations print the days leading up to harvest:

- [ft_count_harvest_iterative.py](python_module_00/ex6/ft_count_harvest_iterative.py) uses a `while` loop.
- [ft_count_harvest_recursive.py](python_module_00/ex6/ft_count_harvest_recursive.py) uses a nested recursive function and a stopping condition.

Comparing them demonstrates two ways to express repeated work.

</details>

<details>
<summary>Exercise 07: Seed Inventory</summary>

[ft_seed_inventory.py](python_module_00/ex7/ft_seed_inventory.py) accepts a seed type, quantity, and unit as typed parameters. It formats inventory messages for packets, grams, or covered area, with a fallback for unknown units.

</details>

</details>

---

<details>
<summary><strong>Python - Module 01: Garden Objects</strong></summary>

Classes, instance attributes, constructors, encapsulation, inheritance, method overriding, nested classes, static methods, and class methods.

<details>
<summary>Exercise 00: Garden Introduction</summary>

[ft_garden_intro.py](python_module_01/ex0/ft_garden_intro.py) displays a plant's name, height, and age using ordinary variables. It establishes the data that later exercises organize into objects.

</details>

<details>
<summary>Exercise 01: Garden Data</summary>

[ft_garden_data.py](python_module_01/ex1/ft_garden_data.py) introduces a `Plant` class with a constructor and a display method. Multiple instances keep their own names, heights, and ages.

</details>

<details>
<summary>Exercise 02: Plant Growth</summary>

[ft_plant_growth.py](python_module_01/ex2/ft_plant_growth.py) adds aging and growth behavior to plants. A weekly simulation updates their state and reports the change in height.

</details>

<details>
<summary>Exercise 03: Plant Factory</summary>

[ft_plant_factory.py](python_module_01/ex3/ft_plant_factory.py) constructs a collection of plants with different initial attributes. Iterating over the collection demonstrates how one class can represent many independent objects.

</details>

<details>
<summary>Exercise 04: Garden Security</summary>

[ft_garden_security.py](python_module_01/ex4/ft_garden_security.py) introduces encapsulation through attributes marked with a leading underscore and explicit getters and setters. The setters reject negative ages and heights, keeping invalid values out of the plant's state.

</details>

<details>
<summary>Exercise 05: Plant Types</summary>

[ft_plant_types.py](python_module_01/ex5/ft_plant_types.py) specializes `Plant` into `Flower`, `Tree`, and `Vegetable`. The subclasses add features such as blooming, shade production, harvest seasons, and nutritional values while reusing shared plant behavior through inheritance and `super()`.

</details>

<details>
<summary>Exercise 06: Garden Analytics</summary>

[ft_garden_analytics.py](python_module_01/ex6/ft_garden_analytics.py) extends the hierarchy with a `Seed` subclass and nested statistics classes. It tracks actions such as growth, aging, and display, and demonstrates a static age check, a class method for creating an anonymous plant, and polymorphic statistics reporting.

</details>

</details>

---

<details>
<summary><strong>Python - Module 02: Garden Error Handling</strong></summary>

Exception handling with `try`/`except`, explicit validation with `raise`, custom exception hierarchies, and cleanup with `finally`.

<details>
<summary>Exercise 00: First Exception</summary>

[ft_first_exception.py](python_module_02/ex0/ft_first_exception.py) converts temperature strings to integers and catches `ValueError` for invalid input. The demonstration processes both valid and invalid values without terminating unexpectedly.

</details>

<details>
<summary>Exercise 01: Raise an Exception</summary>

[ft_raise_exception.py](python_module_02/ex1/ft_raise_exception.py) adds temperature limits to the conversion function. Values below 0°C or above 40°C explicitly raise `ValueError` with a message explaining the problem.

</details>

<details>
<summary>Exercise 02: Different Error Types</summary>

[ft_different_errors.py](python_module_02/ex2/ft_different_errors.py) deliberately triggers `ValueError`, `ZeroDivisionError`, `FileNotFoundError`, and `TypeError`. It demonstrates catching several exception types together and handling specific types separately.

</details>

<details>
<summary>Exercise 03: Custom Errors</summary>

[ft_custom_errors.py](python_module_02/ex3/ft_custom_errors.py) defines `GardenError` and its `PlantError` and `WaterError` subclasses. The demonstration catches individual errors and then handles both subclasses through their shared parent type.

</details>

<details>
<summary>Exercise 04: The Finally Block</summary>

[ft_finally_block.py](python_module_02/ex4/ft_finally_block.py) simulates opening a watering system, watering plants, and closing it. The closing step runs in `finally`, including when an invalid plant name interrupts watering.

</details>

</details>

---

<details>
<summary><strong>Python - Module 03: Game Data Analytics</strong></summary>

Command-line arguments, lists, tuples, sets, dictionaries, generators, and comprehensions.

<details>
<summary>Exercise 00: Command Quest</summary>

[ft_command_quest.py](python_module_03/ex0/ft_command_quest.py) inspects `sys.argv` to display the program name and supplied arguments. It distinguishes user arguments from the complete argument list, which also includes the script name.

</details>

<details>
<summary>Exercise 01: Score Analytics</summary>

[ft_score_analytics.py](python_module_03/ex1/ft_score_analytics.py) builds a list of integer scores from command-line arguments and skips invalid values. It reports the player count, total, average, highest and lowest scores, and score range.

```bash
python3 python_module_03/ex1/ft_score_analytics.py 100 250 75 invalid
```

</details>

<details>
<summary>Exercise 02: Coordinate System</summary>

[ft_coordinate_system.py](python_module_03/ex2/ft_coordinate_system.py) reads two three-dimensional positions in `x,y,z` format and stores them as tuples. It validates the input and calculates the first position's distance from the origin and the distance between both positions.

</details>

<details>
<summary>Exercise 03: Achievement Tracker</summary>

[ft_achievement_tracker.py](python_module_03/ex3/ft_achievement_tracker.py) generates achievement sets for several players. Set union, intersection, and difference identify all unlocked achievements, shared achievements, player-specific achievements, and missing achievements.

</details>

<details>
<summary>Exercise 04: Inventory System</summary>

[ft_inventory_system.py](python_module_03/ex4/ft_inventory_system.py) parses `item:quantity` arguments into a dictionary. It reports quantities, inventory percentages, and the most and least abundant items, while handling malformed arguments and duplicate names.

```bash
python3 python_module_03/ex4/ft_inventory_system.py sword:1 potion:5 shield:2
```

</details>

<details>
<summary>Exercise 05: Data Stream</summary>

[ft_data_stream.py](python_module_03/ex5/ft_data_stream.py) uses `yield` to generate random player events on demand. A second generator consumes events from a stored list, illustrating the difference between producing a stream and processing an existing collection.

</details>

<details>
<summary>Exercise 06: Data Alchemist</summary>

[ft_data_alchemist.py](python_module_03/ex6/ft_data_alchemist.py) uses list and dictionary comprehensions to normalize names, filter players, generate scores, and select above-average results. It combines transformation and filtering with aggregate calculations.

</details>

</details>

---

<details>
<summary><strong>Python - Module 04: Cyber Archives</strong></summary>

Reading and writing text files, handling operating-system errors, managing standard streams, and closing resources reliably.

<details>
<summary>Exercise 00: Ancient Text</summary>

[ft_ancient_text.py](python_module_04/ex0/ft_ancient_text.py) opens a file supplied on the command line and prints its contents. It handles `OSError` and closes the file in a `finally` block.

```bash
python3 python_module_04/ex0/ft_ancient_text.py README.md
```

</details>

<details>
<summary>Exercise 01: Archive Creation</summary>

[ft_archive_creation.py](python_module_04/ex1/ft_archive_creation.py) reads an existing archive, appends a `#` marker to each line, and prompts for an output filename. An empty filename skips saving; otherwise, the transformed text is written to the chosen file.

</details>

<details>
<summary>Exercise 02: Stream Management</summary>

[ft_stream_management.py](python_module_04/ex2/ft_stream_management.py) performs the archive transformation using `sys.stdin`, `sys.stdout`, and `sys.stderr`. It separates normal output from error messages and flushes the prompt before reading input.

</details>

<details>
<summary>Exercise 03: Vault Security</summary>

[ft_vault_security.py](python_module_04/ex3/ft_vault_security.py) provides a `secure_archive()` helper for reading and writing files with a `with` context manager. It returns a success flag and a result or error message, and demonstrates handling missing or inaccessible files.

The demonstration looks for `text.txt` in the current working directory and writes `text_copy.txt` if the read succeeds.

</details>

</details>

---

<details>
<summary><strong>Python - Module 05: Code Nexus</strong></summary>

Abstract base classes, polymorphic processing, heterogeneous data streams, and extensible output through protocols.

<details>
<summary>Exercise 00: Data Processor</summary>

[data_processor.py](python_module_05/ex0/data_processor.py) defines an abstract `DataProcessor` with shared output behavior and abstract validation and ingestion methods. `NumericProcessor`, `TextProcessor`, and `LogProcessor` implement the interface for their own data types, storing numbered output entries and rejecting invalid input.

</details>

<details>
<summary>Exercise 01: Data Stream</summary>

[data_stream.py](python_module_05/ex1/data_stream.py) adds a `DataStream` that registers processors and routes each input to the first processor that accepts it. It reports unsupported items and displays how many entries each processor has handled and still holds.

</details>

<details>
<summary>Exercise 02: Data Pipeline</summary>

[data_pipeline.py](python_module_05/ex2/data_pipeline.py) extends the stream with an output pipeline and an `ExportPlugin` protocol. CSV and JSON plugins format batches of processed entries, including escaping special characters, demonstrating how output behavior can be added through a common interface.

</details>

</details>

---

<details>
<summary><strong>Python - Module 06: Alchemy and Imports</strong></summary>

Module imports, package initialization, exported names, aliases, absolute and relative imports, and circular dependencies.

This module groups its demonstrations by name rather than using `ex0`, `ex1`, and similar folders.

<details>
<summary>Alembic: Modules and Package Exports</summary>

The [ft_alembic_*.py scripts](python_module_06/) compare `import module` with `from module import name`, first using the local `elements.py` and then the `alchemy` package. The package's `__init__.py` exposes selected functions at package level.

`ft_alembic_4.py` intentionally attempts to access `alchemy.create_earth`, which has not been exposed at that level, and raises `AttributeError`.

</details>

<details>
<summary>Distillation: Import Aliases</summary>

[ft_distillation_0.py](python_module_06/ft_distillation_0.py) imports potion functions directly from `alchemy.potions`. [ft_distillation_1.py](python_module_06/ft_distillation_1.py) accesses them through the package, where `healing_potion` is exposed under the alias `heal`.

</details>

<details>
<summary>Transmutation: Nested Packages</summary>

The [ft_transmutation_*.py scripts](python_module_06/) call the same `lead_to_gold()` recipe through its module, its subpackage, and the top-level `alchemy` package. The implementation combines absolute and relative imports, while package initializers make the recipe accessible at different levels.

</details>

<details>
<summary>Kaboom: Circular Imports</summary>

[ft_kaboom_0.py](python_module_06/ft_kaboom_0.py) demonstrates a working spellbook that delays an import until the function is called. [ft_kaboom_1.py](python_module_06/ft_kaboom_1.py) deliberately imports a spellbook with a circular dependency, producing an uncaught import error.

The paired implementations show how import timing affects access to partially initialized modules.

</details>

</details>

---

<details>
<summary><strong>Python - Module 07: Creature Factories and Battle Strategies</strong></summary>

Abstract interfaces, the abstract factory pattern, multiple inheritance, capability checks, and interchangeable strategies.

<details>
<summary>Exercise 00: Creature Factories</summary>

[ex0](python_module_07/ex0/) defines abstract `Creature` and `CreatureFactory` classes. Flame and aqua factories create related base and evolved creatures, each providing its own attack behavior.

[battle.py](python_module_07/battle.py) demonstrates both factories and a simple encounter:

```bash
python3 python_module_07/battle.py
```

</details>

<details>
<summary>Exercise 01: Healing and Transformation</summary>

[ex1](python_module_07/ex1/) adds `HealCapability` and `TransformCapability` interfaces. New creatures combine the shared creature interface with healing or transformation through multiple inheritance, and corresponding factories create their base and evolved forms.

[capacitor.py](python_module_07/capacitor.py) demonstrates the additional capabilities:

```bash
python3 python_module_07/capacitor.py
```

</details>

<details>
<summary>Exercise 02: Battle Strategies</summary>

[ex2](python_module_07/ex2/) introduces a `BattleStrategy` interface with normal, aggressive, and defensive implementations. Aggressive strategies require transformation, defensive strategies require healing, and incompatible combinations raise `InvalidStrategyError`.

[tournament.py](python_module_07/tournament.py) assembles factories and strategies into encounters, including an example that handles an invalid pairing:

```bash
python3 python_module_07/tournament.py
```

</details>

</details>

---

<details>
<summary><strong>Python - Module 08: Inside the Matrix</strong></summary>

Virtual environments, dependency management with pip and Poetry, data analysis, plotting, and configuration through environment variables.

<details>
<summary>Exercise 00: The Construct</summary>

[construct.py](python_module_08/ex0/construct.py) compares `sys.prefix` and `sys.base_prefix` to detect whether Python is running inside a virtual environment. It displays the interpreter, environment information, and package installation paths, with setup instructions when no environment is active.

</details>

<details>
<summary>Exercise 01: Loading Programs</summary>

[loading.py](python_module_08/ex1/loading.py) checks for NumPy, pandas, and Matplotlib and displays their installed versions. It generates 1,000 random values, prints summary statistics, and saves a histogram as `matrix_analysis.png` in the current working directory.

Dependencies are declared in both [requirements.txt](python_module_08/ex1/requirements.txt) and [pyproject.toml](python_module_08/ex1/pyproject.toml). Poetry commands should be run from `python_module_08/ex1/`.

</details>

<details>
<summary>Exercise 02: The Oracle</summary>

[oracle.py](python_module_08/ex2/oracle.py) loads configuration with `python-dotenv` and `os.getenv()`. It reads `MATRIX_MODE`, `DATABASE_URL`, `API_KEY`, `LOG_LEVEL`, and `ZION_ENDPOINT`, reports their configuration status, and checks for missing production settings.

Values can come from environment variables or a local `.env` file. With no configuration, it uses development mode and the `INFO` log level.

</details>

</details>

---

<details>
<summary><strong>Python - Module 09: Space Data Validation</strong></summary>

Pydantic v2 models, field constraints, optional values, enumerations, nested models, and validation rules involving multiple fields.

<details>
<summary>Exercise 00: Space Station</summary>

[space_station.py](python_module_09/ex0/space_station.py) models station data with `BaseModel` and `Field`. Constraints limit identifiers, names, crew size, power, and oxygen levels, while optional notes and default operational status demonstrate additional model features.

The demonstration creates a valid station and catches a `ValidationError` for an oversized crew.

</details>

<details>
<summary>Exercise 01: Alien Contact</summary>

[alien_contact.py](python_module_09/ex1/alien_contact.py) combines an enum for contact types with an `AlienContact` model. An after-model validator checks ID prefixes, verification for physical contact, witness counts for telepathic contact, and message requirements for strong signals.

</details>

<details>
<summary>Exercise 02: Space Crew</summary>

[space_crew.py](python_module_09/ex2/space_crew.py) nests a list of `CrewMember` models inside `SpaceMission`. Mission validation requires a captain or commander, active crew members, and sufficient experienced members for missions longer than a year.

The example creates a valid Mars mission and demonstrates rejection of a crew without a qualifying commanding officer.

</details>

</details>

---

<details>
<summary><strong>Python - Module 10: FuncMage Chronicles</strong></summary>

Lambda expressions, higher-order functions, closures, persistent local state, utilities from `functools`, and decorators.

<details>
<summary>Exercise 00: Lambda Spells</summary>

[lambda_spells.py](python_module_10/ex0/lambda_spells.py) uses lambda expressions with `sorted()`, `filter()`, and `map()` to order artifacts, select powerful mages, and transform spell names. Additional statistics report the maximum, minimum, and average mage power.

</details>

<details>
<summary>Exercise 01: Higher Magic</summary>

[higher_magic.py](python_module_10/ex1/higher_magic.py) accepts functions as arguments and returns new callables. Helpers combine two spells, amplify power, apply a casting condition, and execute a sequence of spells against the same target.

</details>

<details>
<summary>Exercise 02: Scope Mysteries</summary>

[scope_mysteries.py](python_module_10/ex2/scope_mysteries.py) uses closures to retain state after the outer function returns. A counter and power accumulator update captured variables with `nonlocal`, an enchantment factory captures configuration, and a memory vault shares stored data between two returned functions.

</details>

<details>
<summary>Exercise 03: Functools Artifacts</summary>

[functools_artifacts.py](python_module_10/ex3/functools_artifacts.py) explores four tools from `functools`:

- `reduce()` combines spell powers using addition, multiplication, minimum, or maximum.
- `partial()` creates enchantment functions with preset arguments.
- `lru_cache()` memoizes recursive Fibonacci calculations.
- `singledispatch()` selects spell behavior based on the first argument's type.

</details>

<details>
<summary>Exercise 04: Decorator Mastery</summary>

[decorator_mastery.py](python_module_10/ex4/decorator_mastery.py) implements decorators for execution timing, minimum-power validation, and retrying failed calls. `functools.wraps()` preserves wrapped function metadata, and the `MageGuild` class demonstrates decorated instance methods alongside a static name validator.

</details>

[data_generator.py](python_module_10/data_generator.py) provides an interactive helper for generating sample mages, artifacts, spells, and other exercise data:

```bash
python3 python_module_10/data_generator.py
```

</details>
