
Public Class Form1

    Dim L = New Integer() {0, 0, 0, 0, 0, 0, 0, 0, 0}
    Dim C As Integer = 1

    Function CHECK(V As Integer) As Integer
        Dim S As Integer = 0
        If (L(0) = 1 And L(3) = 1 And L(6) = 1) Or (L(1) = 1 And L(4) = 1 And L(7) = 1) Or (L(2) = 1 And L(5) = 1 And L(8) = 1) Then
            S = 1
        ElseIf (L(0) = 1 And L(1) = 1 And L(2) = 1) Or (L(3) = 1 And L(4) = 1 And L(5) = 1) Or (L(6) = 1 And L(7) = 1 And L(8) = 1) Then
            S = 1
        ElseIf (L(0) = 1 And L(4) = 1 And L(8) = 1) Or (L(2) = 1 And L(4) = 1 And L(6) = 1) Then
            S = 1
        End If

        If (L(0) = 2 And L(3) = 2 And L(6) = 2) Or (L(1) = 2 And L(4) = 2 And L(7) = 2) Or (L(2) = 2 And L(5) = 2 And L(8) = 2) Then
            S = 2
        ElseIf (L(0) = 2 And L(1) = 2 And L(2) = 2) Or (L(3) = 2 And L(4) = 2 And L(5) = 2) Or (L(6) = 2 And L(7) = 2 And L(8) = 2) Then
            S = 2
        ElseIf (L(0) = 2 And L(4) = 2 And L(8) = 2) Or (L(2) = 2 And L(4) = 2 And L(6) = 2) Then
            S = 2
        End If

        Return S
    End Function

    Function STOPGAME(V As Integer) As Integer
        Dim G As Integer = 1
        For i = 0 To 8
            If L(i) = 0 Then
                G = 0
            End If
        Next
        Return G
    End Function

    Private Sub Form1_Load(sender As Object, e As EventArgs) Handles MyBase.Load
        Button1.BackColor = Color.White
        Button2.BackColor = Color.White
        Button3.BackColor = Color.White
        Button4.BackColor = Color.White
        Button5.BackColor = Color.White
        Button6.BackColor = Color.White
        Button7.BackColor = Color.White
        Button8.BackColor = Color.White
        Button9.BackColor = Color.White

        Button1.Enabled = False
        Button2.Enabled = False
        Button3.Enabled = False
        Button4.Enabled = False
        Button5.Enabled = False
        Button6.Enabled = False
        Button7.Enabled = False
        Button8.Enabled = False
        Button9.Enabled = False
        Button13.Enabled = False

        Button10.Enabled = False

        Button12.BackColor = Color.FloralWhite
        Button13.BackColor = Color.FloralWhite

        MessageBox.Show("兩位玩家分別點擊 FIRST 和 SECOND 後，即可開始遊戲~")
    End Sub


    Private Sub Button10_Click(sender As Object, e As EventArgs) Handles Button10.Click  'RESTART
        Button1.BackColor = Color.White
        Button2.BackColor = Color.White
        Button3.BackColor = Color.White
        Button4.BackColor = Color.White
        Button5.BackColor = Color.White
        Button6.BackColor = Color.White
        Button7.BackColor = Color.White
        Button8.BackColor = Color.White
        Button9.BackColor = Color.White

        Button1.Enabled = True
        Button2.Enabled = True
        Button3.Enabled = True
        Button4.Enabled = True
        Button5.Enabled = True
        Button6.Enabled = True
        Button7.Enabled = True
        Button8.Enabled = True
        Button9.Enabled = True
        C = 1

        L = {0, 0, 0, 0, 0, 0, 0, 0, 0}

        Button10.Enabled = False
    End Sub

    '''----------------------
    Private Sub Button1_Click(sender As Object, e As EventArgs) Handles Button1.Click
        If (C Mod 2) = 1 Then
            Button1.BackColor = Color.Red
            L(0) = 1
        Else
            Button1.BackColor = Color.Blue
            L(0) = 2
        End If
        C = C + 1

        If CHECK(5) = 1 Then
            MessageBox.Show("R WIN!")
        ElseIf CHECK(5) = 2 Then
            MessageBox.Show("B WIN!")
        End If

        If (STOPGAME(5) = 1) Or (CHECK(5) = 1) Or (CHECK(5) = 2) Then
            Button1.Enabled = False
            Button2.Enabled = False
            Button3.Enabled = False
            Button4.Enabled = False
            Button5.Enabled = False
            Button6.Enabled = False
            Button7.Enabled = False
            Button8.Enabled = False
            Button9.Enabled = False
            Button13.Enabled = False
            Button10.Enabled = True
        End If
    End Sub
    Private Sub Button2_Click(sender As Object, e As EventArgs) Handles Button2.Click
        If (C Mod 2) = 1 Then
            Button2.BackColor = Color.Red
            L(1) = 1
        Else
            Button2.BackColor = Color.Blue
            L(1) = 2
        End If
        C = C + 1

        If CHECK(5) = 1 Then
            MessageBox.Show("R WIN!")
        ElseIf CHECK(5) = 2 Then
            MessageBox.Show("B WIN!")
        End If

        If (STOPGAME(5) = 1) Or (CHECK(5) = 1) Or (CHECK(5) = 2) Then
            Button1.Enabled = False
            Button2.Enabled = False
            Button3.Enabled = False
            Button4.Enabled = False
            Button5.Enabled = False
            Button6.Enabled = False
            Button7.Enabled = False
            Button8.Enabled = False
            Button9.Enabled = False
            Button13.Enabled = False
            Button10.Enabled = True
        End If
    End Sub
    Private Sub Button3_Click(sender As Object, e As EventArgs) Handles Button3.Click
        If (C Mod 2) = 1 Then
            Button3.BackColor = Color.Red
            L(2) = 1
        Else
            Button3.BackColor = Color.Blue
            L(2) = 2
        End If
        C = C + 1

        If CHECK(5) = 1 Then
            MessageBox.Show("R WIN!")
        ElseIf CHECK(5) = 2 Then
            MessageBox.Show("B WIN!")
        End If

        If (STOPGAME(5) = 1) Or (CHECK(5) = 1) Or (CHECK(5) = 2) Then
            Button1.Enabled = False
            Button2.Enabled = False
            Button3.Enabled = False
            Button4.Enabled = False
            Button5.Enabled = False
            Button6.Enabled = False
            Button7.Enabled = False
            Button8.Enabled = False
            Button9.Enabled = False
            Button13.Enabled = False
            Button10.Enabled = True
        End If
    End Sub
    Private Sub Button4_Click(sender As Object, e As EventArgs) Handles Button4.Click
        If (C Mod 2) = 1 Then
            Button4.BackColor = Color.Red
            L(3) = 1
        Else
            Button4.BackColor = Color.Blue
            L(3) = 2
        End If
        C = C + 1

        If CHECK(5) = 1 Then
            MessageBox.Show("R WIN!")
        ElseIf CHECK(5) = 2 Then
            MessageBox.Show("B WIN!")
        End If

        If (STOPGAME(5) = 1) Or (CHECK(5) = 1) Or (CHECK(5) = 2) Then
            Button1.Enabled = False
            Button2.Enabled = False
            Button3.Enabled = False
            Button4.Enabled = False
            Button5.Enabled = False
            Button6.Enabled = False
            Button7.Enabled = False
            Button8.Enabled = False
            Button9.Enabled = False
            Button13.Enabled = False
            Button10.Enabled = True
        End If
    End Sub
    Private Sub Button5_Click(sender As Object, e As EventArgs) Handles Button5.Click
        If (C Mod 2) = 1 Then
            Button5.BackColor = Color.Red
            L(4) = 1
        Else
            Button5.BackColor = Color.Blue
            L(4) = 2
        End If
        C = C + 1

        If CHECK(5) = 1 Then
            MessageBox.Show("R WIN!")
        ElseIf CHECK(5) = 2 Then
            MessageBox.Show("B WIN!")
        End If

        If (STOPGAME(5) = 1) Or (CHECK(5) = 1) Or (CHECK(5) = 2) Then
            Button1.Enabled = False
            Button2.Enabled = False
            Button3.Enabled = False
            Button4.Enabled = False
            Button5.Enabled = False
            Button6.Enabled = False
            Button7.Enabled = False
            Button8.Enabled = False
            Button9.Enabled = False
            Button13.Enabled = False
            Button10.Enabled = True
        End If
    End Sub
    Private Sub Button6_Click(sender As Object, e As EventArgs) Handles Button6.Click
        If (C Mod 2) = 1 Then
            Button6.BackColor = Color.Red
            L(5) = 1
        Else
            Button6.BackColor = Color.Blue
            L(5) = 2
        End If
        C = C + 1

        If CHECK(5) = 1 Then
            MessageBox.Show("R WIN!")
        ElseIf CHECK(5) = 2 Then
            MessageBox.Show("B WIN!")
        End If

        If (STOPGAME(5) = 1) Or (CHECK(5) = 1) Or (CHECK(5) = 2) Then
            Button1.Enabled = False
            Button2.Enabled = False
            Button3.Enabled = False
            Button4.Enabled = False
            Button5.Enabled = False
            Button6.Enabled = False
            Button7.Enabled = False
            Button8.Enabled = False
            Button9.Enabled = False
            Button13.Enabled = False
            Button10.Enabled = True
        End If
    End Sub
    Private Sub Button7_Click(sender As Object, e As EventArgs) Handles Button7.Click
        If (C Mod 2) = 1 Then
            Button7.BackColor = Color.Red
            L(6) = 1
        Else
            Button7.BackColor = Color.Blue
            L(6) = 2
        End If
        C = C + 1

        If CHECK(5) = 1 Then
            MessageBox.Show("R WIN!")
        ElseIf CHECK(5) = 2 Then
            MessageBox.Show("B WIN!")
        End If

        If (STOPGAME(5) = 1) Or (CHECK(5) = 1) Or (CHECK(5) = 2) Then
            Button1.Enabled = False
            Button2.Enabled = False
            Button3.Enabled = False
            Button4.Enabled = False
            Button5.Enabled = False
            Button6.Enabled = False
            Button7.Enabled = False
            Button8.Enabled = False
            Button9.Enabled = False
            Button13.Enabled = False
            Button10.Enabled = True
        End If
    End Sub
    Private Sub Button8_Click(sender As Object, e As EventArgs) Handles Button8.Click
        If (C Mod 2) = 1 Then
            Button8.BackColor = Color.Red
            L(7) = 1
        Else
            Button8.BackColor = Color.Blue
            L(7) = 2
        End If
        C = C + 1

        If CHECK(5) = 1 Then
            MessageBox.Show("R WIN!")
        ElseIf CHECK(5) = 2 Then
            MessageBox.Show("B WIN!")
        End If

        If (STOPGAME(5) = 1) Or (CHECK(5) = 1) Or (CHECK(5) = 2) Then
            Button1.Enabled = False
            Button2.Enabled = False
            Button3.Enabled = False
            Button4.Enabled = False
            Button5.Enabled = False
            Button6.Enabled = False
            Button7.Enabled = False
            Button8.Enabled = False
            Button9.Enabled = False
            Button13.Enabled = False
            Button10.Enabled = True
        End If
    End Sub
    Private Sub Button9_Click(sender As Object, e As EventArgs) Handles Button9.Click
        If (C Mod 2) = 1 Then
            Button9.BackColor = Color.Red
            L(8) = 1
        Else
            Button9.BackColor = Color.Blue
            L(8) = 2
        End If
        C = C + 1

        If CHECK(5) = 1 Then
            MessageBox.Show("R WIN!")
        ElseIf CHECK(5) = 2 Then
            MessageBox.Show("B WIN!")
        End If

        If (STOPGAME(5) = 1) Or (CHECK(5) = 1) Or (CHECK(5) = 2) Then
            Button1.Enabled = False
            Button2.Enabled = False
            Button3.Enabled = False
            Button4.Enabled = False
            Button5.Enabled = False
            Button6.Enabled = False
            Button7.Enabled = False
            Button8.Enabled = False
            Button9.Enabled = False
            Button13.Enabled = False
            Button10.Enabled = True
        End If
    End Sub

    Private Sub Button12_Click(sender As Object, e As EventArgs) Handles Button12.Click
        Button12.BackColor = Color.Red
        Button13.Enabled = True
    End Sub

    Private Sub Button13_Click(sender As Object, e As EventArgs) Handles Button13.Click
        Button13.BackColor = Color.Blue

        Button1.Enabled = True
        Button2.Enabled = True
        Button3.Enabled = True
        Button4.Enabled = True
        Button5.Enabled = True
        Button6.Enabled = True
        Button7.Enabled = True
        Button8.Enabled = True
        Button9.Enabled = True
    End Sub


End Class

