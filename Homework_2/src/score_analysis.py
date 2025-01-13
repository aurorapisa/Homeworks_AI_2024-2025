import numpy as np
import matplotlib.pyplot as plt

def analyze_scores(scores):
    """Task: Analyze student performance across multiple subjects"""

    """
    # Step 1
    Calculate statistics for:
        - Each student's average performance
        - Each subject's average scores
        - Overall class performance
    """

    # Student's average performance
    student_average = np.mean(scores, axis=1)

    # Subject's average scores
    subject_average = np.mean(scores, axis=0)

    # Overall class performance
    overall_average = np.mean(student_average)

    """
    # Step 2
    Analyze score distribution:
        - Calculate standard deviation
        - Identify highest and lowest performing students
        - Determine score ranges for each subject
    """

    # Standard deviation
    student_std = np.std(scores, axis=1)

    # Highest and lowest performing students
    highest_performing_student = np.argmax(student_average)
    lowest_performing_student = np.argmin(student_average)

    # Score range for each subject
    subject_ranges = np.ptp(scores, axis=0)

    # Prepare the statistics dictionary
    stats_dict = {
        'student_average': student_average,
        'subject_average': subject_average,
        'overall_average': overall_average,
        'student_std': student_std,
        'highest_performing_student': highest_performing_student,
        'lowest_performing_student': lowest_performing_student,
        'subject_ranges': subject_ranges
    }

    """
    # Step 3
    Create visualizations:
        - Bar plot of student averages with error bars
        - Subject performance comparison
        - Score distribution histogram
        - Box plot for each subject
    """

    plt.figure(figsize=(12, 8))

    # 1. Bar plot of student averages with error bars
    plt.subplot(2, 2, 1)
    plt.bar(range(len(student_average)), student_average, yerr=student_std, capsize=5, color='blue')
    plt.title('Student averages with error bars')
    plt.xlabel('Student')
    plt.ylabel('Average Score')

    print("Student averages with error bars:")
    for i, avg in enumerate(student_average):
        print(f"Student {i + 1}: Average = {avg:.2f}, Standard deviation = {student_std[i]:.2f}")

    # 2. Bar plot for subject performance comparison
    plt.subplot(2, 2, 2)
    plt.bar(range(len(subject_average)), subject_average, color='green')
    plt.title('Subject performance comparison')
    plt.xlabel('Subject')
    plt.ylabel('Average Score')

    print("\nSubject performance comparison:")
    for i, avg in enumerate(subject_average):
        print(f"Subject {i + 1}: Average = {avg:.2f}")

    # 3. Histogram of student score distribution
    plt.subplot(2, 2, 3)
    plt.hist(student_average, color='orange', edgecolor='black')
    plt.title('Student score distribution')
    plt.xlabel('Average Score')
    plt.ylabel('Frequency')

    print("\nStudent score distribution:")
    print(f"Overall class performance = {overall_average:.2f}")

    # 4. Box plot per ogni soggetto
    plt.subplot(2, 2, 4)
    plt.boxplot(scores, vert=False, patch_artist=True, flierprops=dict(marker='o', color='gray', markersize=0))
    plt.title('Range for each subject')
    plt.xlabel('Score')
    plt.yticks([i + 1 for i in range(scores.shape[1])], [f'Subject {i + 1}' for i in range(scores.shape[1])])

    plt.tight_layout()
    plt.show()

    pass