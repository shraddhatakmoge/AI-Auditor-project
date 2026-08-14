import streamlit as st

from app.auditor.final_audit import FinalAuditor


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="AI Decision Auditor",
    page_icon="🧠",
    layout="wide"
)


# =========================================================
# CACHE AUDITOR
# =========================================================

@st.cache_resource
def get_auditor():
    return FinalAuditor()


# =========================================================
# STYLING
# =========================================================

st.markdown("""
<style>

.block-container {
    max-width: 1100px;
    padding-top: 2rem;
}

.hero-title {
    font-size: 44px;
    font-weight: 700;
    margin-bottom: 5px;
}

.hero-subtitle {
    color: #9ca3af;
    font-size: 17px;
    line-height: 1.6;
    margin-bottom: 30px;
}

.card {
    padding: 20px;
    border-radius: 14px;
    border: 1px solid #30343b;
    background: #161a21;
    margin-bottom: 15px;
}

.risk-score {
    font-size: 40px;
    font-weight: 700;
}

.small-label {
    color: #9ca3af;
    font-size: 13px;
    letter-spacing: 0.5px;
}

.evidence-card {
    padding: 18px;
    border-radius: 12px;
    border: 1px solid #30343b;
    background: #161a21;
    margin-bottom: 12px;
    line-height: 1.6;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="hero-title">🧠 AI Decision Auditor</div>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="hero-subtitle">
    Thinking about an important decision?
    See what you're assuming, what you're missing,
    what the available evidence says, and what could go wrong
    before you commit to it.
    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.header("🧠 How it helps")

    st.markdown("""
    **Your Decision**

    ↓

    **What You're Assuming**

    ↓

    **What You're Missing**

    ↓

    **What The Evidence Says**

    ↓

    **Another Way To Look At It**

    ↓

    **Decision Risk**
    """)

    st.divider()

    st.caption(
        "Make better-informed decisions by challenging "
        "the reasoning behind them."
    )


# =========================================================
# INPUT
# =========================================================

st.subheader("What decision are you considering?")

decision = st.text_area(
    "Decision",
    placeholder=(
        "Example:\n\n"
        "I should buy the more expensive laptop because "
        "it has a better GPU and I want to use it for AI development."
    ),
    height=160,
    label_visibility="collapsed"
)


# =========================================================
# AUDIT BUTTON
# =========================================================

if st.button(
    "🔍 Audit My Decision",
    type="primary",
    use_container_width=True
):

    if not decision.strip():

        st.warning("Please enter a decision first.")

        st.stop()

    try:

        with st.spinner(
            "Thinking through your decision..."
        ):

            auditor = get_auditor()

            result = auditor.audit(decision)

        st.session_state["audit_result"] = result

    except Exception as e:

        st.error(
            "Something went wrong while auditing your decision."
        )

        with st.expander("Technical Details"):

            st.exception(e)

        st.stop()


# =========================================================
# RESULTS
# =========================================================

if "audit_result" in st.session_state:

    result = st.session_state["audit_result"]

    st.divider()

    st.header("📊 Your Decision Audit")


    # =====================================================
    # SUMMARY
    # =====================================================

    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown(
            f"""
            <div class="card">
                <div class="small-label">AREA</div>
                <h3>{result["domain"]}</h3>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:

        st.markdown(
            f"""
            <div class="card">
                <div class="small-label">DECISION RISK</div>
                <h3>{result["risk"]["level"].upper()}</h3>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:

        st.markdown(
            f"""
            <div class="card">
                <div class="small-label">RISK SCORE</div>
                <div class="risk-score">
                    {result["risk"]["score"]}/10
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )


    # =====================================================
    # YOUR DECISION
    # =====================================================

    st.subheader("🎯 Your Decision")

    st.markdown(
        f"""
        <div class="card">
            {result["decision"]}
        </div>
        """,
        unsafe_allow_html=True
    )


    # =====================================================
    # ASSUMPTIONS
    # =====================================================

    st.subheader("⚠️ What You're Assuming")

    if result["assumptions"]:

        for assumption in result["assumptions"]:

            importance = assumption.importance.upper()

            st.markdown(
                f"""
                <div class="card">
                    <strong>{assumption.text}</strong>
                    <br><br>
                    <span class="small-label">
                        Importance: {importance}
                    </span>
                </div>
                """,
                unsafe_allow_html=True
            )

    else:

        st.info(
            "No major assumptions were identified."
        )


    # =====================================================
    # EXPECTED OUTCOME
    # =====================================================

    st.subheader("🎯 What You Expect To Happen")

    st.markdown(
        f"""
        <div class="card">
            {result["expected_outcome"]}
        </div>
        """,
        unsafe_allow_html=True
    )


    # =====================================================
    # MISSING INFORMATION
    # =====================================================

    st.subheader("❓ What You May Be Missing")

    if result["missing_information"]:

        for item in result["missing_information"]:

            st.markdown(
                f"- {item}"
            )

    else:

        st.success(
            "No major missing information was identified."
        )


    # =====================================================
    # EVIDENCE
    # =====================================================

    st.subheader("📚 What The Evidence Says")

    verification = result["verification"]

    status_text = verification.status.value.replace(
        "_",
        " "
    ).title()

    col1, col2 = st.columns(2)

    with col1:

        st.markdown(
            f"**Evidence strength:** `{status_text}`"
        )

    with col2:

        st.markdown(
            f"**Confidence:** `{verification.confidence:.2f}`"
        )

    st.markdown("### What this means")

    st.write(
        verification.reasoning
    )


    # =====================================================
    # SUPPORTING EVIDENCE
    # =====================================================

    if result["evidence"]:

        st.markdown(
            "### Information considered"
        )

        for document in result["evidence"]:

            st.markdown(
                f"""
                <div class="evidence-card">
                    {document.page_content}
                </div>
                """,
                unsafe_allow_html=True
            )

    else:

        st.warning(
            "No relevant evidence was found."
        )


    # =====================================================
    # COUNTERARGUMENT
    # =====================================================

    st.subheader("⚔️ Another Way To Look At It")

    counterargument = result["counterargument"]

    st.markdown(
        f"""
        <div class="card">

        <strong>What could challenge this decision?</strong>

        <p>
        {counterargument.argument}
        </p>

        <strong>Why it matters</strong>

        <p>
        {counterargument.reasoning}
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )


    # =====================================================
    # RISK ASSESSMENT
    # =====================================================

    st.subheader("🚨 Decision Risk")

    risk = result["risk"]

    st.markdown(
        f"""
        <div class="card">

        <div class="small-label">
            OVERALL RISK
        </div>

        <div class="risk-score">
            {risk["score"]}/10
        </div>

        <h3>
            {risk["level"].upper()}
        </h3>

        </div>
        """,
        unsafe_allow_html=True
    )


    if risk["reasons"]:

        st.markdown(
            "### Why?"
        )

        for reason in risk["reasons"]:

            st.markdown(
                f"- {reason}"
            )