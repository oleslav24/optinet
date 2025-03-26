# Реализация Carbon-Optimized + Hybrid-модели
# Основная идея: на каждом шаге выбираем самый "зелёный" доступный узел и применяем LNN+ZNN адаптацию ресурсов

# Инициализация ресурсов узлов
co_hybrid_resources = {
    node: {"cpu": 100, "memory": 200, "io": 50, "error_cpu": 0, "error_mem": 0, "error_io": 0}
    for node in node_ids
}

adaptation_rate = 0.1
znn_decay = 0.05

co_hybrid_results = []

for i in range(num_tasks):
    node_id = task_node_ids[i]
    arrival = task_timestamps[i]
    cpu = cpu_demand[i]
    mem = memory_demand[i]
    io = io_operations[i]
    energy = total_energy_wh[i]
    priority = priority_level[i]
    carbon = carbon_intensity[i]

    # Найдём все подходящие узлы по ресурсам
    suitable_nodes = [
        (nid, res, node_carbon_intensity_map[nid])
        for nid, res in co_hybrid_resources.items()
        if res["cpu"] >= cpu and res["memory"] >= mem and res["io"] >= io
    ]

    if suitable_nodes:
        # Выбираем самый зелёный доступный узел
        selected_node, selected_res, selected_carbon = min(suitable_nodes, key=lambda x: x[2])
        delay = 0
        executed_time = arrival

        # LNN: адаптация ресурсов вверх
        selected_res["cpu"] += adaptation_rate * cpu
        selected_res["memory"] += adaptation_rate * mem
        selected_res["io"] += adaptation_rate * io

        # ZNN: экспоненциальное затухание ошибки
        selected_res["error_cpu"] *= (1 - znn_decay)
        selected_res["error_mem"] *= (1 - znn_decay)
        selected_res["error_io"] *= (1 - znn_decay)

    else:
        # Задержка, если нет доступных зелёных узлов
        selected_node = "Unassigned"
        selected_carbon = 400
        delay = 5
        executed_time = arrival + pd.Timedelta(minutes=delay)

    # Углеродный след
    carbon_emission = energy * selected_carbon

    co_hybrid_results.append({
        "arrival": arrival,
        "executed_time": executed_time,
        "delay_min": delay,
        "node_id": selected_node,
        "carbon_intensity": selected_carbon,
        "carbon_emission_g": carbon_emission,
        "energy_wh": energy,
        "priority": priority
    })

# Создаем DataFrame результатов
co_hybrid_df = pd.DataFrame(co_hybrid_results)

# Метрики
avg_delay = co_hybrid_df["delay_min"].mean()
total_energy = co_hybrid_df["energy_wh"].sum()
total_co2 = co_hybrid_df["carbon_emission_g"].sum()

summary_co_hybrid = {
    "Total Tasks": len(co_hybrid_df),
    "Average Delay (min)": round(avg_delay, 2),
    "Total Energy (MWh)": round(total_energy / 1e6, 2),
    "Total CO2 Emissions (tonnes)": round(total_co2 / 1e6, 2)
}

import ace_tools as tools; tools.display_dataframe_to_user(name="Carbon-Optimized Hybrid Results", dataframe=co_hybrid_df.sample(1000))

summary_co_hybrid