import streamlit as st
import random

st.set_page_config(page_title="🏇 sugoroku競馬", layout="wide")

BOARD_SIZE = 19

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
def draw_lane(pos, label):
    lane = ["□"] * (BOARD_SIZE + 1)
    lane[pos] = "🏇"
    return f"{label} " + "".join(lane) + " 🏁"

st.markdown("### レース状況")
st.markdown(draw_lane(st.session_state.pos_a, "A"))
st.markdown(draw_lane(st.session_state.pos_b, "B"))



# -------------------------
# サイコロ
# -------------------------
if not st.session_state.finished:
    if st.button("🎲 サイコロを振る"):
        roll = random.randint(1, 6)

        if st.session_state.turn == "A":
            st.session_state.pos_a = min(
                st.session_state.pos_a + roll, BOARD_SIZE
            )
            st.session_state.turn = "B"
        else:
            st.session_state.pos_b = min(
                st.session_state.pos_b + roll, BOARD_SIZE
            )
            st.session_state.turn = "A"

        st.info(f"出目：{roll}")

# -------------------------
# 勝敗判定
# -------------------------
if st.session_state.pos_a >= BOARD_SIZE:
    st.success("🏆 プレイヤーA 勝利！")
    st.session_state.finished = True

if st.session_state.pos_b >= BOARD_SIZE:
    st.success("🏆 プレイヤーB 勝利！")
    st.session_state.finished = True


