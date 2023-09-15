<!DOCTYPE html>
<html>
<head>
    <title>Enkripsi Teks</title>
</head>
<body>
    <h1>Program Enkripsi Teks</h1>

    <?php
    if ($_SERVER['REQUEST_METHOD'] == 'POST') {
        $plaintext = $_POST['plaintext'];
        $encrypted_text = encryptText($plaintext);
    }

    function encryptText($text)
    {
        $char_mapping = [
            'a' => '1',
            'b' => '2',
            'c' => '3',
            'd' => '4',
            'e' => '5',
            'f' => '6',
            'g' => '7',
            'h' => '8',
            'i' => '9',
            'j' => '0',
            'k' => '!',
            'l' => '@',
            'm' => '#',
            'n' => '$',
            'o' => '%',
            'p' => '^',
            'q' => '&',
            'r' => '*',
            's' => '(',
            't' => ')',
            'u' => '-',
            'v' => '+',
            'w' => '=',
            'x' => '[',
            'y' => ']',
            'z' => '{',
            ' ' => ' '
        ];

        $text = strtolower($text);
        $encrypted_text = '';

        for ($i = 0; $i < strlen($text); $i++) {
            $char = $text[$i];
            if (array_key_exists($char, $char_mapping)) {
                $encrypted_text .= $char_mapping[$char];
            } else {
                $encrypted_text .= $char; // Biarkan karakter seperti itu jika tidak ada dalam daftar enkripsi
            }
        }

        return $encrypted_text;
    }
    ?>

    <form method="post" action="">
        <label for="plaintext">Masukkan teks plainteks:</label>
        <input type="text" id="plaintext" name="plaintext" required>
        <button type="submit">Enkripsi</button>
    </form>

    <?php
    if (isset($encrypted_text)) {
        echo "<p>Teks terenkripsi: $encrypted_text</p>";
    }
    ?>

</body>
</html>
