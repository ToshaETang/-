Imports System.IO
Imports System.Math
Imports System.Data.Entity.dll


Public Class Form1
    Public MyFN As String
    Public MyImg(,,)
    Public MyRow, MyCol As Integer
    Public MyXll, MyYll, Cellsize As Single
    Public NoData As Integer
    Public MyBnd As Integer
    Public NNoData As Integer
    Public MyNDVI(,) As Single
    Public MyTMP1(), MyTMP2(), MyTMP3(), MyTMP4(), MyTMP5(), MyTMP6(), MyTMP7() As String
    Public MyStr1, MyStr2, MyStr3, MyStr4, MyStr5, MyStr6, MyStr7 As String
    Public AVE As Double = 0
    Public S As Double = 0   'SD
    Public V As Double = 0



    Private Sub TrackBar1_Scroll(sender As Object, e As EventArgs) Handles TrackBar1.Scroll
        V = Val(TrackBar1.Value) / 100
        TextBox1.Text = Str(V)
    End Sub

    Private Sub Button1_Click(sender As Object, e As EventArgs) Handles Button1.Click
        End
    End Sub


    Private Sub OPENToolStripMenuItem_Click(sender As Object, e As EventArgs) Handles OPENToolStripMenuItem.Click
        Dim MyFN1, MyFN2, MyFN3, MyFN4, MyFN5, MyFN6, MyFN7 As String
        OpenFileDialog5.Filter = ("csv CSV| *.csv")
        OpenFileDialog5.FileName = ""
        Dim N As Integer

        If Not OpenFileDialog5.ShowDialog = DialogResult.Cancel Then     '''開檔案
            MyFN = OpenFileDialog5.FileName
            N = MyFN.Length - 5
            MyFN1 = MyFN.Substring(0, N) + "1.csv"
            MyFN2 = MyFN.Substring(0, N) + "2.csv"
            MyFN3 = MyFN.Substring(0, N) + "3.csv"
            MyFN4 = MyFN.Substring(0, N) + "4.csv"
            MyFN5 = MyFN.Substring(0, N) + "5.csv"
            MyFN6 = MyFN.Substring(0, N) + "6.csv"
            MyFN7 = MyFN.Substring(0, N) + "7.csv"

            RichTextBox1.AppendText("Reading multispectrum image data from files : " + vbNewLine)
            RichTextBox1.AppendText(MyFN1 + vbNewLine)
            RichTextBox1.AppendText(MyFN2 + vbNewLine)
            RichTextBox1.AppendText(MyFN3 + vbNewLine)
            RichTextBox1.AppendText(MyFN4 + vbNewLine)
            RichTextBox1.AppendText(MyFN5 + vbNewLine)
            RichTextBox1.AppendText(MyFN6 + vbNewLine)
            RichTextBox1.AppendText(MyFN7 + vbNewLine)
            RichTextBox1.AppendText("--------------------------------------------------------" + vbNewLine)
            Dim MyRD1 = New StreamReader(MyFN1)
            Dim MyRD2 = New StreamReader(MyFN2)
            Dim MyRD3 = New StreamReader(MyFN3)
            Dim MyRD4 = New StreamReader(MyFN4)
            Dim MyRD5 = New StreamReader(MyFN5)
            Dim MyRD6 = New StreamReader(MyFN6)
            Dim MyRD7 = New StreamReader(MyFN7)
            Dim MyK As Integer
            Dim MyPa(6) As Integer
            For MyK = 0 To 5
                MyStr1 = MyRD1.ReadLine
                MyStr2 = MyRD2.ReadLine
                MyStr3 = MyRD3.ReadLine
                MyStr4 = MyRD4.ReadLine
                MyStr5 = MyRD5.ReadLine
                MyStr6 = MyRD6.ReadLine
                MyStr7 = MyRD7.ReadLine
                RichTextBox1.AppendText(MyStr1 + vbNewLine)
                MyTMP1 = Split(MyStr1, ",")
                MyPa(MyK) = Val(MyTMP1(1))
            Next
            MyCol = MyPa(0)
            MyRow = MyPa(1)
            MyXll = MyPa(2)
            MyYll = MyPa(3)
            Cellsize = MyPa(4)
            NoData = MyPa(5)
            Dim MyBMP As Bitmap = New Bitmap(MyCol, MyRow)
            ReDim MyImg(3, MyRow, MyCol)
            Dim RR, GG, BB As Integer
            Dim MyColor As Color
            Dim II, JJ, KK As Integer
            For II = 0 To MyRow - 1
                MyStr1 = MyRD1.ReadLine
                MyStr2 = MyRD2.ReadLine
                MyStr3 = MyRD3.ReadLine
                MyTMP1 = Split(MyStr1, ",")
                MyTMP2 = Split(MyStr2, ",")
                MyTMP3 = Split(MyStr3, ",")
                For JJ = 0 To MyCol - 1
                    MyImg(0, II, JJ) = Val(MyTMP1(JJ))
                    MyImg(1, II, JJ) = Val(MyTMP2(JJ))
                    MyImg(2, II, JJ) = Val(MyTMP3(JJ))
                    If MyImg(0, II, JJ) = 0 Then
                        RR = 255
                        GG = 255
                        BB = 255
                    Else
                        RR = MyImg(0, II, JJ)
                        GG = MyImg(1, II, JJ)
                        BB = MyImg(2, II, JJ)
                    End If
                    If RR = -9999 Then
                        RR = 255
                        GG = 255
                        BB = 255
                    End If
                    MyColor = Color.FromArgb(RR, GG, BB)
                    MyBMP.SetPixel(JJ, II, MyColor)
                Next
            Next
            PictureBox1.SizeMode = PictureBoxSizeMode.Zoom
            PictureBox1.Image = MyBMP
            MyRD1.Close()
            MyRD2.Close()
            MyRD3.Close()
        End If
    End Sub


    '算表面溫度
    Private Sub CALCULATEToolStripMenuItem_Click(sender As Object, e As EventArgs) Handles CALCULATEToolStripMenuItem.Click
        Dim Lmin As Double = 1.238
        Dim Lmax As Double = 15.6
        Dim FN6 As String
        Dim LL As String

        Dim MyVFN As String = "C:\Users\Tosha.E.T\Desktop\大二下\#地理程式設計應用\FINAL_DATA\表面溫度.csv"
        Dim MyWriter = New StreamWriter(MyVFN)
        Dim MyStr As String

        OpenFileDialog4.Filter = ("csv CSV| *.csv")
        OpenFileDialog4.FileName = ""

        MyStr = "cols" + "," + Str("2882")
        MyWriter.WriteLine(MyStr)
        MyStr = "rows" + "," + Str("2758")
        MyWriter.WriteLine(MyStr)
        MyStr = "XLL" + "," + Str("278856.2115")
        MyWriter.WriteLine(MyStr)
        MyStr = "YLL" + "," + Str("2729962.321")
        MyWriter.WriteLine(MyStr)
        MyStr = "cellsize" + "," + Str("25")
        MyWriter.WriteLine(MyStr)
        MyStr = "NoData" + "," + Str(NoData)
        MyWriter.WriteLine(MyStr)

        If Not OpenFileDialog4.ShowDialog = DialogResult.Cancel Then
            FN6 = OpenFileDialog4.FileName
            Dim MyRD6 = New StreamReader(FN6)
            For i = 0 To 2757
                MyStr6 = MyRD6.ReadLine
                MyTMP6 = Split(MyStr6, ",")
                LL = ""
                If i > 5 Then
                    For j = 0 To 2881
                        LL = LL + Str(((1260.56 / (Log((607.76 / (Lmin + (Lmax - Lmin) * Val(MyTMP6(j)) / 255)) + 1)))) - 273.15) + ","
                    Next
                    MyStr = LL
                    MyWriter.WriteLine(MyStr)
                End If
            Next
        End If
        MyWriter.Close()
        RichTextBox1.AppendText("-----表面溫度 SAVE!!!-----" + vbNewLine)
    End Sub


    'NDVI
    Private Sub NDVIToolStripMenuItem_Click(sender As Object, e As EventArgs) Handles NDVIToolStripMenuItem.Click
        Dim FNb3, FNb4 As String
        Dim MyVFN As String = "C:\Users\Tosha.E.T\Desktop\大二下\#地理程式設計應用\FINAL_DATA\NDVI.csv"
        Dim MyWriter = New StreamWriter(MyVFN)
        Dim MyStr, MyStr3, MyStr4 As String
        Dim LL As String

        OpenFileDialog1.Filter = ("csv CSV| *.csv")
        OpenFileDialog1.FileName = ""
        OpenFileDialog2.Filter = ("csv CSV| *.csv")
        OpenFileDialog2.FileName = ""

        MyStr = "cols" + "," + Str("2882")
        MyWriter.WriteLine(MyStr)
        MyStr = "rows" + "," + Str("2758")
        MyWriter.WriteLine(MyStr)
        MyStr = "XLL" + "," + Str("278856.2115")
        MyWriter.WriteLine(MyStr)
        MyStr = "YLL" + "," + Str("2729962.321")
        MyWriter.WriteLine(MyStr)
        MyStr = "cellsize" + "," + Str("25")
        MyWriter.WriteLine(MyStr)
        MyStr = "NoData" + "," + Str(NoData)
        MyWriter.WriteLine(MyStr)

        If Not OpenFileDialog1.ShowDialog = DialogResult.Cancel Then
            FNb3 = OpenFileDialog1.FileName
            Dim RDb3 = New StreamReader(FNb3)
            If Not OpenFileDialog2.ShowDialog = DialogResult.Cancel Then
                FNb4 = OpenFileDialog2.FileName
                Dim RDb4 = New StreamReader(FNb4)
                For i = 0 To 2757
                    MyStr3 = RDb3.ReadLine
                    MyStr4 = RDb4.ReadLine
                    MyTMP3 = Split(MyStr3, ",")
                    MyTMP4 = Split(MyStr4, ",")
                    LL = ""
                    If i > 5 Then
                        For j = 0 To 2881
                            LL = LL + Str((Val(MyTMP4(j)) - Val(MyTMP3(j))) / (Val(MyTMP4(j)) + Val(MyTMP3(j)))) + ","
                        Next
                        MyStr = LL
                        MyWriter.WriteLine(MyStr)
                    End If
                Next
            End If
        End If
        MyWriter.Close()
        RichTextBox1.AppendText("-----NDVI SAVE!!!-----" + vbNewLine)
    End Sub


    '地表平均溫帶+標準差
    Private Sub ATSDToolStripMenuItem_Click(sender As Object, e As EventArgs) Handles ATSDToolStripMenuItem.Click
        Dim FN As String
        Dim LL As New List(Of Double)
        Dim MyTMPAS() As String

        Dim MyVFN As String = "C:\Users\Tosha.E.T\Desktop\大二下\#地理程式設計應用\FINAL_DATA\AT+SD.csv"
        Dim MyWriter As New StreamWriter(MyVFN)
        Dim MyStr, MyStrAS As String

        OpenFileDialog3.Filter = ("csv CSV| *.csv")
        OpenFileDialog3.FileName = ""

        If Not OpenFileDialog3.ShowDialog = DialogResult.Cancel Then
            FN = OpenFileDialog3.FileName
            Dim MyRD = New StreamReader(FN)
            For i = 0 To 2757
                MyStrAS = MyRD.ReadLine
                MyTMPAS = Split(MyStrAS, ",")
                If i > 5 Then
                    For j = 0 To 2881
                        Try
                            LL.Add(Val(MyTMPAS(j)))
                        Catch ex As Exception
                        End Try
                    Next

                End If
            Next
        End If

        Dim LL2 As New List(Of Double)
        For i = 0 To (LL.Count - 1)
            AVE = AVE + LL(i)
        Next
        AVE = AVE / LL.Count
        MyStr = "AT" + "," + Str(AVE)
        MyWriter.WriteLine(MyStr)       '平均溫度
        For i = 0 To (LL.Count - 1)
            S = S + ((LL(i) - AVE) * (LL(i) - AVE))
        Next
        S = Sqrt(S / LL.Count)
        MyStr = "SD" + "," + Str(S)    '標準差:計算各數值與平均數的差，取其平方後加總，再除以數值個數，得「變異數」。變異數開根號後得「標準差」
        MyWriter.WriteLine(MyStr)
        MyWriter.Close()
        RichTextBox1.AppendText("-----AT+SD SAVE!!!-----" + vbNewLine)
    End Sub

    '找熱島
    Private Sub HeatIslandToolStripMenuItem_Click(sender As Object, e As EventArgs) Handles HeatIslandToolStripMenuItem.Click
        Dim FN As String
        Dim MyTMPHI() As String
        Dim MyVFN As String = "C:\Users\Tosha.E.T\Desktop\大二下\#地理程式設計應用\FINAL_DATA\熱島.csv"
        Dim MyWriter As New StreamWriter(MyVFN)
        Dim MyStr, MyStrHI As String
        Dim LL As String
        Dim H As Double = 0

        OpenFileDialog6.Filter = ("csv CSV| *.csv")
        OpenFileDialog6.FileName = ""

        MyStr = "cols" + "," + Str("2882")
        MyWriter.WriteLine(MyStr)
        MyStr = "rows" + "," + Str("2758")
        MyWriter.WriteLine(MyStr)
        MyStr = "XLL" + "," + Str("278856.2115")
        MyWriter.WriteLine(MyStr)
        MyStr = "YLL" + "," + Str("2729962.321")
        MyWriter.WriteLine(MyStr)
        MyStr = "cellsize" + "," + Str("25")
        MyWriter.WriteLine(MyStr)
        MyStr = "NoData" + "," + Str("0")
        MyWriter.WriteLine(MyStr)

        If Not OpenFileDialog6.ShowDialog = DialogResult.Cancel Then
            FN = OpenFileDialog6.FileName
            Dim MyRD = New StreamReader(FN)
            For i = 0 To 2757
                MyStrHI = MyRD.ReadLine
                MyTMPHI = Split(MyStrHI, ",")
                LL = ""
                If i > 5 Then
                    For j = 0 To 2881
                        Try
                            H = Val(MyTMPHI(j))
                            If H > (1.5 * Val(S)) Then
                                LL = LL + Str(H) + ","
                            Else
                                LL = LL + Str("0") + ","
                            End If
                        Catch ex As Exception

                        End Try
                    Next
                    MyStr = LL
                    MyWriter.WriteLine(MyStr)
                End If
            Next
        End If
        MyWriter.Close()
        RichTextBox1.AppendText("-----熱島 SAVE!!!-----" + vbNewLine)
    End Sub


    '植被分布
    Private Sub VegetationToolStripMenuItem_Click(sender As Object, e As EventArgs) Handles VegetationToolStripMenuItem.Click
        Dim FN As String
        Dim MyTMPV() As String
        Dim MyVFN As String = "C:\Users\Tosha.E.T\Desktop\大二下\#地理程式設計應用\FINAL_DATA\植被分布.csv"
        Dim MyWriter As New StreamWriter(MyVFN)
        Dim MyStr, MyStrV As String
        Dim LL As String
        Dim H As Double = 0

        OpenFileDialog7.Filter = ("csv CSV| *.csv")
        OpenFileDialog7.FileName = ""

        MyStr = "cols" + "," + Str("2882")
        MyWriter.WriteLine(MyStr)
        MyStr = "rows" + "," + Str("2758")
        MyWriter.WriteLine(MyStr)
        MyStr = "XLL" + "," + Str("278856.2115")
        MyWriter.WriteLine(MyStr)
        MyStr = "YLL" + "," + Str("2729962.321")
        MyWriter.WriteLine(MyStr)
        MyStr = "cellsize" + "," + Str("25")
        MyWriter.WriteLine(MyStr)
        MyStr = "NoData" + "," + Str("0")
        MyWriter.WriteLine(MyStr)

        If Not OpenFileDialog7.ShowDialog = DialogResult.Cancel Then
            FN = OpenFileDialog7.FileName
            Dim MyRD = New StreamReader(FN)
            For i = 0 To 2757
                MyStrV = MyRD.ReadLine
                MyTMPV = Split(MyStrV, ",")
                LL = ""
                If i > 5 Then
                    For j = 0 To 2881
                        Try
                            H = Val(MyTMPV(j))
                            If H > V Then
                                LL = LL + Str(H) + ","
                            Else
                                LL = LL + Str("0") + ","
                            End If
                        Catch ex As Exception

                        End Try
                    Next
                    MyStr = LL
                    MyWriter.WriteLine(MyStr)
                End If
            Next
        End If
        MyWriter.Close()
        RichTextBox1.AppendText("-----植被分布 SAVE!!!-----" + vbNewLine)
    End Sub
    '''''''''''''''''''''''''''''''''''做完了'''''''''''''''''''''''''''''''''''
End Class




