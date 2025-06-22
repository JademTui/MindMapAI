from modules.auto_evolve_worker import main_loop

if __name__ == "__main__":
    # Run only 1 iteration for testing
    main_loop(interval_minutes=0, max_iterations=1)
