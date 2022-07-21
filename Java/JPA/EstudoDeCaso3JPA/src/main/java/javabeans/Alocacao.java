package javabeans;

import java.io.Serializable;
import java.util.Objects;
import javax.persistence.CascadeType;
import javax.persistence.Entity;
import javax.persistence.FetchType;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.ManyToOne;
import javax.persistence.Version;

@Entity
public class Alocacao implements Serializable {

    private static final long serialVersionUID = 1L;
    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    private Long id;

    @Id
    @ManyToOne(cascade = CascadeType.ALL, fetch = FetchType.EAGER)
    @JoinColumn(name = "id_enfermeiro", nullable = false)
    private Enfermeiro enfermeiro;
    
    @Id
    @ManyToOne(cascade = CascadeType.ALL, fetch = FetchType.EAGER)
    @JoinColumn(name = "id_enfermaria", nullable = false)
    private Enfermaria enfermaria;
    
    @Version
    private int versao;

    public Alocacao() {
        this.id = 0L;
        this.enfermeiro = null;
        this.enfermaria = null;
    }
    
    

    public Alocacao(Long id, Enfermeiro enfermeiro, Enfermaria enfermaria, int versao) {
        this.id = id;
        this.enfermeiro = enfermeiro;
        this.enfermaria = enfermaria;
        this.versao = versao;
    }

    
    
    @Override
    public int hashCode() {
        int hash = 7;
        hash = 23 * hash + Objects.hashCode(this.id);
        hash = 23 * hash + Objects.hashCode(this.enfermeiro);
        hash = 23 * hash + Objects.hashCode(this.enfermaria);
        hash = 23 * hash + this.versao;
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
        final Alocacao other = (Alocacao) obj;
        if (this.versao != other.versao) {
            return false;
        }
        if (!Objects.equals(this.id, other.id)) {
            return false;
        }
        if (!Objects.equals(this.enfermeiro, other.enfermeiro)) {
            return false;
        }
        if (!Objects.equals(this.enfermaria, other.enfermaria)) {
            return false;
        }
        return true;
    }

    
    
    public Enfermeiro getEnfermeiro() {
        return enfermeiro;
    }

    public void setEnfermeiro(Enfermeiro enfermeiro) {
        this.enfermeiro = enfermeiro;
    }

    public Enfermaria getEnfermaria() {
        return enfermaria;
    }

    public void setEnfermaria(Enfermaria enfermaria) {
        this.enfermaria = enfermaria;
    }

    public int getVersao() {
        return versao;
    }

    public void setVersao(int versao) {
        this.versao = versao;
    }
    
    
    
    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    @Override
    public String toString() {
        return this.id.toString();
    }
    
}
