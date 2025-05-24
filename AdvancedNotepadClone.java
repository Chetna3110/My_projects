import javax.swing.*;
import javax.swing.event.DocumentEvent;
import javax.swing.event.DocumentListener;
import javax.swing.text.DefaultEditorKit;
import javax.swing.undo.CannotRedoException;
import javax.swing.undo.CannotUndoException;
import javax.swing.undo.UndoManager;
import java.awt.*;
import java.awt.event.*;
import java.io.*;
import java.util.ArrayList;

public class AdvancedNotepadClone extends JFrame {
    JTabbedPane tabbedPane;
    JLabel statusLabel;
    ArrayList<JTextArea> textAreas = new ArrayList<>();
    UndoManager undoManager = new UndoManager();

    public AdvancedNotepadClone() {
        setTitle("Advanced Notepad Clone");
        setSize(800, 600);
        setDefaultCloseOperation(EXIT_ON_CLOSE);

        tabbedPane = new JTabbedPane();
        addNewTab();

        add(tabbedPane);
        createMenuBar();
        createStatusBar();

        setVisible(true);
    }

    void createStatusBar() {
        statusLabel = new JLabel("Words: 0  Characters: 0");
        add(statusLabel, BorderLayout.SOUTH);
    }

    void updateStatusBar(JTextArea textArea) {
        String text = textArea.getText();
        int wordCount = text.isEmpty() ? 0 : text.split("\\s+").length;
        int charCount = text.length();
        statusLabel.setText("Words: " + wordCount + "  Characters: " + charCount);
    }

    void addNewTab() {
        JTextArea textArea = new JTextArea();
        textArea.setLineWrap(true);
        textArea.setWrapStyleWord(true);
        JScrollPane scrollPane = new JScrollPane(textArea);

        textArea.getDocument().addDocumentListener(new DocumentListener() {
            public void insertUpdate(DocumentEvent e) { updateStatusBar(textArea); }
            public void removeUpdate(DocumentEvent e) { updateStatusBar(textArea); }
            public void changedUpdate(DocumentEvent e) { updateStatusBar(textArea); }
        });

        textArea.getDocument().addUndoableEditListener(undoManager);

        tabbedPane.addTab("Untitled", scrollPane);
        textAreas.add(textArea);
    }

    JTextArea getCurrentTextArea() {
        JScrollPane scrollPane = (JScrollPane) tabbedPane.getSelectedComponent();
        return textAreas.get(tabbedPane.getSelectedIndex());
    }

    void createMenuBar() {
        JMenuBar menuBar = new JMenuBar();

        JMenu fileMenu = new JMenu("File");
        JMenuItem newTab = new JMenuItem("New Tab");
        JMenuItem open = new JMenuItem("Open");
        JMenuItem save = new JMenuItem("Save");
        JMenuItem print = new JMenuItem("Print");
        JMenuItem exit = new JMenuItem("Exit");

        newTab.addActionListener(e -> addNewTab());
        open.addActionListener(e -> openFile());
        save.addActionListener(e -> saveFile());
        print.addActionListener(e -> {
            try {
                getCurrentTextArea().print();
            } catch (Exception ex) {
                ex.printStackTrace();
            }
        });
        exit.addActionListener(e -> System.exit(0));

        fileMenu.add(newTab);
        fileMenu.add(open);
        fileMenu.add(save);
        fileMenu.add(print);
        fileMenu.addSeparator();
        fileMenu.add(exit);

        JMenu editMenu = new JMenu("Edit");
        JMenuItem undo = new JMenuItem("Undo");
        JMenuItem redo = new JMenuItem("Redo");
        JMenuItem cut = new JMenuItem(new DefaultEditorKit.CutAction());
        JMenuItem copy = new JMenuItem(new DefaultEditorKit.CopyAction());
        JMenuItem paste = new JMenuItem(new DefaultEditorKit.PasteAction());
        JMenuItem findReplace = new JMenuItem("Find/Replace");

        undo.addActionListener(e -> {
            try { undoManager.undo(); } catch (CannotUndoException ex) {}
        });
        redo.addActionListener(e -> {
            try { undoManager.redo(); } catch (CannotRedoException ex) {}
        });
        findReplace.addActionListener(e -> openFindReplaceDialog());

        editMenu.add(undo);
        editMenu.add(redo);
        editMenu.add(cut);
        editMenu.add(copy);
        editMenu.add(paste);
        editMenu.add(findReplace);

        JMenu viewMenu = new JMenu("View");
        JCheckBoxMenuItem darkMode = new JCheckBoxMenuItem("Dark Mode");
        darkMode.addActionListener(e -> {
            JTextArea ta = getCurrentTextArea();
            if (darkMode.isSelected()) {
                ta.setBackground(Color.BLACK);
                ta.setForeground(Color.WHITE);
                ta.setCaretColor(Color.WHITE);
            } else {
                ta.setBackground(Color.WHITE);
                ta.setForeground(Color.BLACK);
                ta.setCaretColor(Color.BLACK);
            }
        });
        viewMenu.add(darkMode);

        menuBar.add(fileMenu);
        menuBar.add(editMenu);
        menuBar.add(viewMenu);
        setJMenuBar(menuBar);
    }

    void openFile() {
        JFileChooser fileChooser = new JFileChooser();
        if (fileChooser.showOpenDialog(this) == JFileChooser.APPROVE_OPTION) {
            File file = fileChooser.getSelectedFile();
            try (BufferedReader br = new BufferedReader(new FileReader(file))) {
                JTextArea textArea = getCurrentTextArea();
                textArea.read(br, null);
                tabbedPane.setTitleAt(tabbedPane.getSelectedIndex(), file.getName());
            } catch (IOException ex) {
                ex.printStackTrace();
            }
        }
    }

    void saveFile() {
        JFileChooser fileChooser = new JFileChooser();
        if (fileChooser.showSaveDialog(this) == JFileChooser.APPROVE_OPTION) {
            File file = fileChooser.getSelectedFile();
            try (BufferedWriter bw = new BufferedWriter(new FileWriter(file))) {
                JTextArea textArea = getCurrentTextArea();
                textArea.write(bw);
                tabbedPane.setTitleAt(tabbedPane.getSelectedIndex(), file.getName());
            } catch (IOException ex) {
                ex.printStackTrace();
            }
        }
    }

    void openFindReplaceDialog() {
        JTextArea textArea = getCurrentTextArea();
        JDialog dialog = new JDialog(this, "Find and Replace", false);
        dialog.setSize(400, 150);
        dialog.setLayout(new GridLayout(3, 2));

        JTextField findField = new JTextField();
        JTextField replaceField = new JTextField();
        JButton findBtn = new JButton("Find");
        JButton replaceBtn = new JButton("Replace All");

        findBtn.addActionListener(e -> {
            String text = textArea.getText();
            String find = findField.getText();
            int index = text.indexOf(find);
            if (index >= 0) textArea.select(index, index + find.length());
        });

        replaceBtn.addActionListener(e -> {
            String find = findField.getText();
            String replace = replaceField.getText();
            textArea.setText(textArea.getText().replace(find, replace));
        });

        dialog.add(new JLabel("Find:"));
        dialog.add(findField);
        dialog.add(new JLabel("Replace with:"));
        dialog.add(replaceField);
        dialog.add(findBtn);
        dialog.add(replaceBtn);

        dialog.setVisible(true);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(AdvancedNotepadClone::new);
    }
}
