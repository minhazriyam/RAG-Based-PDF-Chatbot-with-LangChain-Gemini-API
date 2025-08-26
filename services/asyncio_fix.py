def ensure_event_loop():
    import asyncio
    try:
        asyncio.get_running_loop()
    except RuntimeError:
        asyncio.set_event_loop(asyncio.new_event_loop())
    try:
        import nest_asyncio
        nest_asyncio.apply()
    except Exception:
        pass
