Feature: Compteur
  Tester les fonctionnalités d'un compteur.

  Scenario Outline: Augmenter ou réduire le compteur
    Given l'application est lancée
    When je clique sur "<action>"
    Then le compteur doit afficher "Compteur : <valeur_attendue>"

    Examples:
      | action       | valeur_attendue |
      | Augmenter    | 1               |
      | Réduire      | -1              |

  Scenario Outline: Tester les limites
    Given l'application est lancée
    When je saisis "<valeur_max>" dans "Valeur maximale :"
    And je saisis "<valeur_min>" dans "Valeur minimale :"
    And je clique sur "Définir les limites"
    And je clique sur "<action>"
    And je clique sur "<action>"
    Then le compteur doit afficher "Compteur : <valeur_attendue>"

    Examples:
      | valeur_max | valeur_min | action       | valeur_attendue |
      | 1          | -1         | Augmenter    | 1               |
      | 1          | -1         | Réduire      | -1              |

  Scenario Outline: Réinitialiser le compteur
    Given l'application est lancée
    When je clique sur "<action>"
    And je clique sur "Réinitialiser"
    Then le compteur doit afficher "Compteur : 0"

    Examples:
      | action    |
      | Augmenter |
      | Réduire   |
