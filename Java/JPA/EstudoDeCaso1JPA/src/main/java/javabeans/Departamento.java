package javabeans;

import java.io.Serializable;
import java.util.Objects;
import javax.persistence.CascadeType;
import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.FetchType;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.OneToOne;

@Entity
public class Departamento implements Serializable {

    private static final long serialVersionUID = 1L;
    
    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    private Long id;
    
    @Column(length = 25, nullable = false, unique = true)
    private String nome;
    
    @Column(nullable = false, unique = true)
    private int numero;
   
    @OneToOne(cascade = CascadeType.ALL, fetch = FetchType.LAZY)
    @JoinColumn(name = "id_gerente", nullable = false, unique = true)
    private Empregado gerente;

    public Departamento() {
        this.id = 0L;
        this.nome = "";
        this.numero = 0;
        this.gerente = null;
    }

    public Departamento(Long id, String nome, int numero, Empregado gerente) {
        this.id = id;
        this.nome = nome;
        this.numero = numero;
        this.gerente = gerente;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public int getNumero() {
        return numero;
    }

    public void setNumero(int numero) {
        this.numero = numero;
    }

    public Empregado getGerente() {
        return gerente;
    }

    public void setGerente(Empregado gerente) {
        this.gerente = gerente;
    }
    
    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    @Override
    public int hashCode() {
        int hash = 7;
        hash = 97 * hash + Objects.hashCode(this.id);
        hash = 97 * hash + Objects.hashCode(this.nome);
        hash = 97 * hash + this.numero;
        hash = 97 * hash + Objects.hashCode(this.gerente);
        return hash;
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) {
            return true;
        }
        if (obj == null) {
            return false;
        }
        if (getClass() != obj.getClass()) {
            return false;
        }
        final Departamento other = (Departamento) obj;
        if (this.numero != other.numero) {
            return false;
        }
        if (!Objects.equals(this.nome, other.nome)) {
            return false;
        }
        if (!Objects.equals(this.id, other.id)) {
            return false;
        }
        if (!Objects.equals(this.gerente, other.gerente)) {
            return false;
        }
        return true;
    }

    @Override
    public String toString() {
        return this.nome;
    }
    
}
