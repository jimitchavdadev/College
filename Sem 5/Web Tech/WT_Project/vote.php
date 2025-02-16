<?php
include 'db_connection.php';

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $voter_id = 1; // Normally fetched from session or login system
    $candidate_id = $_POST['candidate_id'];

    // Check if voter has already voted
    $check_query = "SELECT * FROM votes WHERE voter_id = $voter_id";
    $check_result = mysqli_query($conn, $check_query);

    if (mysqli_num_rows($check_result) > 0) {
        echo "You have already voted.";
    } else {
        $vote_query = "INSERT INTO votes (voter_id, candidate_id) VALUES ($voter_id, $candidate_id)";
        if (mysqli_query($conn, $vote_query)) {
            // Increment candidate vote count
            $update_vote_query = "UPDATE candidates SET votes = votes + 1 WHERE candidate_id = $candidate_id";
            mysqli_query($conn, $update_vote_query);
            echo "Vote recorded successfully!";
        } else {
            echo "Error: " . mysqli_error($conn);
        }
    }
}
?>
