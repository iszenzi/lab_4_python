import src.simulation as sim
from src.book import FictionBook


class TestSimulation:
    """Тесты для симуляции"""

    def test_run_simulation(self, monkeypatch, capsys):
        counter = {"n": 0}

        def fake_generate_random_book():
            counter["n"] += 1
            return FictionBook(
                f"Title{counter['n']}",
                "Author",
                2020 + (counter["n"] % 3),
                "Genre",
                f"987-4567890{counter['n']:03d}",
            )

        monkeypatch.setattr(sim, "generate_random_book", fake_generate_random_book)

        sim.run_simulation(steps=5, seed=123)

        out = capsys.readouterr().out
        assert "Добавление начальных книг в библиотеку:" in out
        assert out.count("Добавлена книга:") >= 5
        assert "НАЧАЛО СИМУЛЯЦИИ" in out
        assert "КОНЕЦ СИМУЛЯЦИИ" in out
