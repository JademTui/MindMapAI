from mindmap_ai import MindMapAI

if __name__ == "__main__":
    app = MindMapAI()
    # Real-world test cases
    print("\n--- Real-World Multi-Agent Organization Test ---\n")

    # 1. Science: Analyze a real-world phenomenon
    print("[Science] Analyze 'photosynthesis':")
    print(app.assign_org_task("science", "analyze", "photosynthesis"))

    # 2. Finance: Query stock market data (simulate query)
    print("\n[Finance] Query stock market data:")
    print(app.assign_org_task("finance", "query", "SELECT * FROM vix LIMIT 1"))

    # 3. History: Retrieve timeline for a major event
    print("\n[History] Timeline for 'Moon Landing':")
    print(app.assign_org_task("history", "timeline", "Moon Landing"))

    # 4. Health: Get info on global pandemic response
    print("\n[Health] Info on 'pandemic response':")
    print(app.assign_org_task("health", "info", "pandemic response"))

    # 5. Technology: Analyze 'AI evolution':
    print("\n[Technology] Analyze 'AI evolution':")
    print(app.assign_org_task("technology", "analyze", "AI evolution"))

    # 6. Mathematics: Solve a real-world math problem
    print("\n[Mathematics] Solve 'integral of x^2':")
    print(app.assign_org_task("mathematics", "solve", "integral of x^2"))

    # 7. Operations: Logistics for 'supply chain':
    print("\n[Operations] Logistics for 'supply chain':")
    print(app.assign_org_task("operations", "logistics", "supply chain"))

    # 8. Arts: Analyze 'Renaissance art':
    print("\n[Arts] Analyze 'Renaissance art':")
    print(app.assign_org_task("arts", "analyze", "Renaissance art"))

    # 9. Knowledge: Country info for 'New Zealand':
    print("\n[Knowledge] Country info for 'New Zealand':")
    print(app.assign_org_task("knowledge", "country_info", "New Zealand"))

    # 10. Advanced Reasoning and Multi-Manager Collaboration
    print("\n--- Advanced Reasoning & Multi-Manager Collaboration ---\n")
    collab_result = app.organization.advanced_collaboration(
        prompt="Devise a coordinated pandemic response using science, technology, and health expertise.",
        involved_manager_names=["science", "technology", "health"],
        context={"scenario": "global pandemic response"}
    )
    print("[Collaboration: Science, Technology, Health]")
    for subject, result in collab_result.items():
        print(f"\n[{subject} Collaboration Result]:\n", result)
