import re


def map_score_to_emoji(score: float) -> str:
    if score <= 1.5:
        return "😢"
    elif score <= 2.5:
        return "😟"
    elif score <= 3.5:
        return "😐"
    elif score <= 4.5:
        return "😊"
    else:
        return "😄"


def plot_sentiment_timeline(scores, chunk_duration_secs=30):
    """
    Improved sentiment timeline plot with emojis, better styling, and clearer axis labels.
    """
    import matplotlib.pyplot as plt
    import matplotlib.ticker as ticker

    x = list(range(len(scores)))
    y = scores

    # Time labels (e.g. 0:00, 0:30, 1:00, etc.)
    time_labels = []
    for i in x:
        total_secs = i * chunk_duration_secs
        mins = total_secs // 60
        secs = total_secs % 60
        time_labels.append(f"{mins}:{secs:02d}")

    # Emojis mapped from score
    emoji_labels = [map_score_to_emoji(score) for score in y]

    plt.figure(figsize=(14, 6))
    plt.plot(x, y, marker='o', markersize=6,
             color='#1f77b4', linewidth=2, alpha=0.8)

    # Add emoji text slightly above each point
    for i, (xi, yi) in enumerate(zip(x, y)):
        plt.text(xi, yi + 0.3, emoji_labels[i], ha='center', fontsize=14)

    plt.title("🎭 Sentiment Timeline (1 = Negative, 5 = Positive)",
              fontsize=14, fontweight='bold', pad=20)
    plt.xlabel("Approximate Time", fontsize=12)
    plt.ylabel("Sentiment Score", fontsize=12)
    plt.xticks(ticks=x, labels=time_labels, rotation=45, fontsize=10)
    plt.yticks(range(1, 6), fontsize=10)

    # Grid and spacing
    plt.grid(visible=True, which='both',
             linestyle='--', linewidth=0.5, alpha=0.7)
    plt.tight_layout()
    plt.savefig("output/sentiment_timeline.png")
    plt.close()
    print("✅ Enhanced sentiment timeline saved as 'sentiment_timeline.png'")


def chunk_transcript(transcript, chunk_size = 5):
    sentences=re.split(r'(?<=[.?!])\s+', transcript.strip())
    return [' '.join(sentences[i:i+chunk_size]) for i in range(0, len(sentences), chunk_size)]


def label_to_score(label):
    try:
        stars=int(label[0])
        return stars
    except:
        return 3  # neutral fallback
