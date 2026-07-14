from pathlib import Path

fight = list(Path("data/rwf2000/Fight").glob("*.avi"))
nonfight = list(Path("data/rwf2000/NonFight").glob("*.avi"))

print(f"Fight videos    : {len(fight)}")
print(f"NonFight videos : {len(nonfight)}")
print(f"Total videos    : {len(fight) + len(nonfight)}")