### End-of-Term Exam: The Academy of Super-Heroes vs. Super-Villain Professors

**Case Context:**

At the heart of the Academy of Super-Heroes, a place where students are trained to become the next generation of humanity’s protectors, a battle is brewing. A series of critical missions (exams) is about to begin, pitting student superheroes against professors who have turned into super-villains for the occasion. As a student and chief developer at the academy, your mission is to create a management system to organize the confrontations, catalog the skills, and strategically plan each superhero's interventions.

**Exam Objective:**

Develop a management system in Python that models the dynamics between superheroes and super-villain professors, using key object-oriented programming concepts to represent the unique characteristics and powers of the participants, as well as the progression of the missions.

**Detailed Instructions:**

**Part 1: UML Design (40 points)**

- **Class Diagram (20 points):**

  - **Class SuperHero:** Should include attributes for name, a list of SuperPower, and a history of completed missions. Methods for adding powers, participating in missions, and displaying hero information.

  - **Class SuperPower:** Represents the heroes' unique powers, with attributes for power name, description, and power level.

  - **Class SuperVillainProf:** Similar to SuperHero, but for professors, including methods to challenge heroes in specific missions.

  - **Class Mission:** Contains information on the challenges to be faced, participants (hero vs. villain), and the outcome of the confrontation.

- **Use Case Diagram (20 points):**

  - Illustrate key interactions: "Plan a mission," where superheroes choose their challenges; "Train a superpower," to improve their skills; and "Confront a super-villain professor," the core of the academic action.

- **Sequence Diagram (20 points):**

  - Illustrate the key interactions between superheroes, super-villain professors, and the mission planning process at the Academy of Super-Heroes.

**Part 2: Development in Python based on correct diagrams (60 points)**

Based on the UML design, implement the system with the following details:

- **Polymorphism:**

  - Specifically with the method `use_power()`.

- **Composition:**

  - Model the relationship between SuperHero and SuperPower.

- **Encapsulation:**

  - Protect the attributes and methods of each class.

**Scenario to Simulate:**

Superheroes plan and execute multiple missions, facing off against super-villain professors in a series of trials designed to test their limits and ingenuity.