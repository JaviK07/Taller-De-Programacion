def dictionary_iteration_and_calculus(rounds):
    """Iterates through a list of dictionaries to obtain round and final rankings."""
    round_values = [3, 1, -1]

    accumulative_deaths = 0

    final_ranking = {}

    for r in rounds:

        ranking_round = {}

        round_points = 0
        max_points = 0
        round_mvp = ''

        print("\n")

        for key, value in r.items():
            k = value['kills'] * round_values[0]
            a = value['assists'] * round_values[1]

            d = round_values[2] if value['deaths'] else 0
            if d == round_values[2]:
                accumulative_deaths += 1

            round_points = k + a + d

            ranking_round[key] = {
                'kills': value['kills'],
                'assists': value['assists'],
                'deaths': 1 if value['deaths'] else 0,
                'round_points': round_points,
                'MVPs': 0  
            }

            if round_points > max_points:
                max_points = round_points
                round_mvp = key
                
            if key not in final_ranking:
                final_ranking[key] = {
                    'Kills': 0,
                    'Assists': 0,
                    'Deaths': 0,
                    'Final Points': 0,
                    'MVPs': 0 
                }

            final_ranking[key]['Kills'] += value['kills']
            final_ranking[key]['Assists'] += value['assists']
            final_ranking[key]['Deaths'] += 1 if value['deaths'] else 0
            final_ranking[key]['Final Points'] += round_points


        if round_mvp:
            final_ranking[round_mvp]['MVPs'] += 1
            ranking_round[round_mvp]['MVPs'] += 1


        ranking_ordered = dict(sorted(ranking_round.items(), key=lambda item: item[1]['round_points'], reverse=True))


        print("________________________________________________")
        print("______________ Round Ranking: ______________")
        print("________________________________________________")
        print(f"{'Player':<10} | {'Kills':<5} | {'Assists':<7} | {'Deaths':<6} | {'Points':<7} | {'MVPs':<4}")
        print("-" * 55)
        for player, stats in ranking_ordered.items():
            print(f"{player:<10} | {stats['kills']:<5} | {stats['assists']:<7} | {str(stats['deaths']):<6} | {stats['round_points']:<7} | {stats['MVPs']:<4}")

    print("\n\n\n")


    final_ranking_ordered = dict(sorted(final_ranking.items(), key=lambda item: item[1]['Final Points'], reverse=True))
    print("________________________________________________")
    print("______________ Final Ranking: ______________")   
    print("________________________________________________")
    print(f"{'Player':<10} | {'Kills':<5} | {'Assists':<7} | {'Deaths':<6} | {'Points':<7} | {'MVPs':<4}")
    print("-" * 55)
    for player, stats in final_ranking_ordered.items():
        print(f"{player:<10} | {stats['Kills']:<5} | {stats['Assists']:<7} | {str(stats['Deaths']):<6} | {stats['Final Points']:<7} | {stats['MVPs']:<4}")