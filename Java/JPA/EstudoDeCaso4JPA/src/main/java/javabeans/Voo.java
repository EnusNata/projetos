package javabeans;

import java.io.Serializable;
import java.util.Date;
import java.util.Objects;
import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.Temporal;
import javax.persistence.TemporalType;
import javax.persistence.Version;

@Entity
public class Voo implements Serializable {

    private static final long serialVersionUID = 1L;
    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    private Long id;

    @Column(nullable = false, unique = true)
    private int numero;
    
    @Temporal(TemporalType.DATE)
    @Column(nullable = false)
    private Date data_voo;
    
    @Column(length = 15, nullable = false)
    private String aeronave;
    
    @Column(length = 25, nullable = false)
    private String origem;
    
    @Column(length = 25, nullable = false)
    private String destino;
    
    @Version
    private int versao;

    public Voo() {
        this.id = 0L;
        this.numero = 0;
        this.data_voo = new Date();
        this.aeronave = "";
        this.origem = "";
        this.destino = "";
        this.versao = 0;
    }

    public Voo(Long id, int numero, Date data_voo, String aeronave, String origem, String destino, int versao) {
        this.id = id;
        this.numero = numero;
        this.data_voo = data_voo;
        this.aeronave = aeronave;
        this.origem = origem;
        this.destino = destino;
        this.versao = versao;
    }
    
    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public int getNumero() {
        return numero;
    }

    public void setNumero(int numero) {
        this.numero = numero;
    }

    public Date getData_voo() {
        return data_voo;
    }

    public void setData_voo(Date data_voo) {
        this.data_voo = data_voo;
    }

    public String getAeronave() {
        return aeronave;
    }

    public void setAeronave(String aeronave) {
        this.aeronave = aeronave;
    }

    public String getOrigem() {
        return origem;
    }

    public void setOrigem(String origem) {
        this.origem = origem;
    }

    public String getDestino() {
        return destino;
    }

    public void setDestino(String destino) {
        this.destino = destino;
    }

    public int getVersao() {
        return versao;
    }

    public void setVersao(int versao) {
        this.versao = versao;
    }

    @Override
    public int hashCode() {
        int hash = 7;
        hash = 41 * hash + Objects.hashCode(this.id);
        hash = 41 * hash + this.numero;
        hash = 41 * hash + Objects.hashCode(this.data_voo);
        hash = 41 * hash + Objects.hashCode(this.aeronave);
        hash = 41 * hash + Objects.hashCode(this.origem);
        hash = 41 * hash + Objects.hashCode(this.destino);
        hash = 41 * hash + this.versao;
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
        final Voo other = (Voo) obj;
        if (this.numero != other.numero) {
            return false;
        }
        if (this.versao != other.versao) {
            return false;
        }
        if (!Objects.equals(this.aeronave, other.aeronave)) {
            return false;
        }
        if (!Objects.equals(this.origem, other.origem)) {
            return false;
        }
        if (!Objects.equals(this.destino, other.destino)) {
            return false;
        }
        if (!Objects.equals(this.id, other.id)) {
            return false;
        }
        if (!Objects.equals(this.data_voo, other.data_voo)) {
            return false;
        }
        return true;
    }
    
    @Override
    public String toString() {
        return Integer.toString(this.numero);
    }
    
}