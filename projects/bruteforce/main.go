package main

import (
	"fmt"
	"math/rand"
	"time"

	"fyne.io/fyne/v2"
	"fyne.io/fyne/v2/app"
	"fyne.io/fyne/v2/container"
	"fyne.io/fyne/v2/widget"
)

func main() {
	rand.Seed(time.Now().Unix())
	myApp := app.New()

	win := myApp.NewWindow("Enter a PIN")
	win.Resize(fyne.NewSize(300, 150)) // Set window size
	content := container.NewGridWithColumns(1)

	attempts := 1
	pinInput := widget.NewEntry()
	pinInput.SetPlaceHolder("0000")
	pinInput.Resize(fyne.NewSize(200, 30)) // Set input size
	submitButton := widget.NewButton("ENTER", func() {})
	label := widget.NewLabel("Enter a PIN:")
	pin := fmt.Sprintf("%04d", rand.Intn(9999))
	submitButton.OnTapped = func() {
		if pinInput.Text == pin {
			label.SetText(fmt.Sprintf("SUCCESS, PIN: %s!", pin))
			content.Remove(submitButton)
			content.Remove(pinInput)
			content.Remove(label)

			successText := widget.NewLabel(fmt.Sprintf(`
CORRECT, THE PIN IS: %s

Now solve this riddle:

 WHERE CAN YOU ALWAYS FIND 'GOLD', 
 BUT THERE'S NO GOLD AT ALL?

`, pin))

			content.Add(successText)
		} else {
			label.SetText(fmt.Sprintf("ERROR ATTEMPT: %d, ENTER PIN:", attempts))
			pinInput.Text = ""
			attempts += 1
		}
	}

	content.Add(label)
	content.Add(pinInput)
	content.Add(submitButton)
	win.SetContent(content)
	win.ShowAndRun()
}
