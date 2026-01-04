import streamlit as st
import random

st.write("🔥 更新テスト 2026-01-03 22:15")

st.set_page_config(page_title="🏇 すごろく競馬", layout="wide")

BOARD_SIZE = 20

# -------------------------
# 初期化
# -------------------------
if "pos_a" not in st.session_state:
    st.session_state.pos_a = 0
if "pos_b" not in st.session_state:
    st.session_state.pos_b = 0
if "turn" not in st.session_state:
    st.session_state.turn = "A"
if "finished" not in st.session_state:
    st.session_state.finished = False

st.title("🏇 すごろく競馬")



# -------------------------
# 盤面描画
# -------------------------
def draw_lane(pos, icon):
    lane = ["＿"] * (BOARD_SIZE + 1)
    lane[pos] = icon
    return "".join(lane) + " 🏁"

st.text(draw_lane(st.session_state.pos_a, "🏇"))
st.text(draw_lane(st.session_state.pos_b, "🏇"))


# -------------------------
# 勝敗判定
# -------------------------
if st.session_state.finished:
    if st.session_state.pos_a >= BOARD_SIZE and st.session_state.pos_b >= BOARD_SIZE:
        st.info("🤝 同着！引き分け！")
    elif st.session_state.pos_a >= BOARD_SIZE:
        st.success("🏆 Aの勝ち！")
    else:
        st.success("🏆 Bの勝ち！")

# -------------------------
# サイコロ
# -------------------------
dice = [1, 2, 3, 4, 5, 6]
BOARD_SIZE = 20

if not st.session_state.finished:
    if st.button("🎲 サイコロを振る（同時）"):
        roll_a = random.choice(dice)
        roll_b = random.choice(dice)

        st.session_state.pos_a += roll_a
        st.session_state.pos_b += roll_b

        st.session_state.pos_a = min(st.session_state.pos_a, BOARD_SIZE)
        st.session_state.pos_b = min(st.session_state.pos_b, BOARD_SIZE)

        st.session_state.last_roll = (roll_a, roll_b)

        # ゴール判定
        if (
            st.session_state.pos_a >= BOARD_SIZE
            or st.session_state.pos_b >= BOARD_SIZE
        ):
            st.session_state.finished = True

        st.rerun()

if "last_roll" in st.session_state:
    a, b = st.session_state.last_roll
    st.write(f"🏇 A：{a}　｜　🏇 B：{b}")

