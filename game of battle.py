import streamlit as st
import random

# ------------------ SETUP ------------------

st.title("Creature Battle Game ⚔️🐉")

# Creatures + Moves
moves = {
    "Dragon": [
        {"name": "Fireball", "damage": 30},
        {"name": "Slash", "damage": 10}
    ],
    "Goat": [
        {"name": "Punch", "damage": 20},
        {"name": "Kick", "damage": 20}
    ]
}

# ------------------ SESSION STATE ------------------

if "player_hp" not in st.session_state:
    st.session_state.player_hp = 100

if "enemy_hp" not in st.session_state:
    st.session_state.enemy_hp = 100

if "game_over" not in st.session_state:
    st.session_state.game_over = False

# ------------------ CHOOSE CREATURE ------------------

choice = st.selectbox("Choose your creature", ["Dragon", "Goat"])

player = choice
enemy = "Goat" if player == "Dragon" else "Dragon"

st.write(f"You chose: **{player}**")
st.write(f"Enemy: **{enemy}**")

# ------------------ HP DISPLAY ------------------

st.write("## HP Status")
st.write(f"Your HP: {st.session_state.player_hp}")
st.write(f"Enemy HP: {st.session_state.enemy_hp}")

# ------------------ MOVE SELECTION ------------------

move_names = [m["name"] for m in moves[player]]
selected_move_name = st.selectbox("Choose your move", move_names)

selected_move = None
for m in moves[player]:
    if m["name"] == selected_move_name:
        selected_move = m

# ------------------ ATTACK BUTTON ------------------

if st.button("Attack ⚔️") and not st.session_state.game_over:

    # Player attack
    st.session_state.enemy_hp -= selected_move["damage"]
    st.write(f"You used {selected_move['name']}!")

    # Check win
    if st.session_state.enemy_hp <= 0:
        st.success("You Win! 🎉")
        st.session_state.game_over = True
        st.stop()

    # Computer attack
    enemy_move = random.choice(moves[enemy])
    st.session_state.player_hp -= enemy_move["damage"]

    st.write(f"Enemy used {enemy_move['name']}!")

    # Check loss
    if st.session_state.player_hp <= 0:
        st.error("You Lose 💀")
        st.session_state.game_over = True
        st.stop()

# ------------------ RESTART ------------------

if st.button("Restart Game 🔄"):
    st.session_state.player_hp = 100
    st.session_state.enemy_hp = 100
    st.session_state.game_over = False
